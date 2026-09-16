import streamlit as st
import pandas as pd

import recommendation_engine

st.write(
    "Recommendation engine loaded from:",
    recommendation_engine.__file__
)

recommend_restaurants = recommendation_engine.recommend_restaurants

st.set_page_config(page_title="Swiggy Restaurant Recommendation System",page_icon="🍽️",layout="wide")

st.title("Swiggy Restaurant Recommendation System")
st.write(
    "Find restaurants based on your preferred "
    "city, cuisine, rating, price and rating count."
)

@st.cache_data
def load_data():
    return pd.read_csv("cleaned_data.csv",index_col=0)

df = load_data()

st.subheader("Enter Your Preferences")
col1,col2 = st.columns(2)

with col1:
    city = st.selectbox("Select City",sorted(df["city"].dropna().unique()))
    cuisine_options = sorted(df["cuisine"].dropna().unique())
    cuisine = st.selectbox("Select cuisine",cuisine_options)
    rating = st.slider("Preferred Rating",min_value=1.0,max_value=5.0,value=4.0,step=0.1)
with col2:
    rating_count = st.number_input("Preferred Rating count",min_value=20,max_value=10000,value=100,step=10)
    cost = st.number_input("Preferred Cost",min_value=50,max_value=8000,value=300,step=50)
    top_n = st.slider("Number of Recommendation",min_value=5,max_value=20,value=10)

if st.button("Get Recommendations",type="primary"):
    with st.spinner("Finding the best restaurants"):
        results = recommend_restaurants(
            city=city,
            cuisine=cuisine,
            rating=rating,
            rating_count=rating_count,
            cost=cost,
            top_n=top_n
        )

    if results.empty:
        st.warning("No restaurants found for the selected city")
    else:
        st.subheader("Recommended Restaurants")
        display_df = results[
            [
                "name",
                "city",
                "rating",
                "rating_count",
                "cost",
                "cuisine",
                "similarity"
            ]
        ].copy()

        display_df["cost"] = (
            "₹" +
            display_df["cost"]
            .round(0)
            .astype(int)
            .astype(str)
        )

        display_df = display_df.rename(
            columns={
                "name": "Restaurant",
                "city": "City",
                "rating": "Rating",
                "rating_count": "Rating Count",
                "cost": "Cost",
                "cuisine": "Cuisine",
                "similarity": "Similarity Score"
            }
        )


        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Similarity Score": st.column_config.NumberColumn(
                    "Similarity Score",
                    format="%.4f"
                ),
                "Rating": st.column_config.NumberColumn(
                    "Rating",
                    format="%.1f"
                ),
                "Rating Count": st.column_config.NumberColumn(
                    "Rating Count",
                    format="%.0f"
        )
    }
)

