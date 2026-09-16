import pandas as pd
import numpy as np
import joblib

from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix, hstack

cleaned_df = pd.read_csv("cleaned_data.csv",index_col=0)

encoder = joblib.load("encoder.pkl")
scaler = joblib.load("scaler.pkl")

categorical_features = ["city","cuisine"]
numerical_features = ["rating","rating_count","cost"]

encoded_cat = encoder.transform(cleaned_df[categorical_features])

scaled_num = scaler.transform(cleaned_df[numerical_features])

numerical_weights = np.array([1.5,0.5,1.5])

scaled_num_weighted = (scaled_num * numerical_weights)

scaled_num_sparse = csr_matrix(scaled_num_weighted)

categorical_weights = np.ones(encoded_cat.shape[1])

feature_names = encoder.get_feature_names_out(categorical_features)

for i, feature in enumerate(feature_names):

    if feature.startswith("city_"):
        categorical_weights[i] = 3.0

    elif feature.startswith("cuisine_"):
        categorical_weights[i] = 3.0

encoded_cat_sparse = csr_matrix(encoded_cat)

encoded_cat_weighted = (encoded_cat_sparse.multiply(categorical_weights))

recommendation_matrix = hstack([scaled_num_sparse,encoded_cat_weighted]).tocsr()

def recommend_restaurants(city,cuisine,rating,rating_count,cost,top_n=10):

    city_mask = (
        cleaned_df["city"]
        .astype(str)
        .str.strip()
        .str.lower()
        == str(city).strip().lower()
    )
    candidate_df = cleaned_df.loc[city_mask].copy()

    candidate_indices = candidate_df.index

    if candidate_df.empty:

        return pd.DataFrame()
    
    candidate_positions = (cleaned_df.index.get_indexer(candidate_df.index))

    candidate_matrix = (recommendation_matrix[candidate_positions])

    user_df = pd.DataFrame({
        "city": [city],
        "cuisine": [cuisine],
        "rating": [rating],
        "rating_count": [rating_count],
        "cost": [cost]
    })

    user_cat = encoder.transform(user_df[categorical_features])

    user_cat_sparse = csr_matrix(user_cat)

    user_cat_weighted = (user_cat_sparse.multiply(categorical_weights))

    user_num = scaler.transform(user_df[numerical_features])

    user_num_weighted = (user_num * numerical_weights)

    user_num_sparse = csr_matrix(user_num_weighted)

    user_vector = hstack([user_num_sparse,user_cat_weighted]).tocsr()

    similarity_scores = cosine_similarity(user_vector,candidate_matrix)[0]

    top_indices = np.argsort(similarity_scores)[::-1][:top_n]

    recommendations = candidate_df.iloc[top_indices].copy()

    recommendations["similarity"] = (similarity_scores[top_indices])

    return recommendations


if __name__ == "__main__":

    results = recommend_restaurants(
        city="Bikaner",
        cuisine="North Indian",
        rating=4.0,
        rating_count=100,
        cost=300,
        top_n=10
    )

    print(
        results[
            [
                "name",
                "city",
                "rating",
                "rating_count",
                "cost",
                "cuisine",
                "similarity"
            ]
        ].to_string(index=False)
    )