# 🍽️ Swiggy Restaurant Recommendation System

A content-based restaurant recommendation system built using **Python, Scikit-learn, Cosine Similarity, and Streamlit**.

The system recommends restaurants based on user preferences such as **city, cuisine, rating, rating count, and cost**. It uses feature-based similarity to identify restaurants that are most similar to the user's selected preferences.

---

## 📌 Project Overview

Finding a suitable restaurant from a large collection of restaurants can be difficult when users have specific preferences.

This project solves the problem by building a recommendation system that:

- Accepts user preferences through a Streamlit web application.
- Filters restaurants based on the selected city.
- Converts categorical features into numerical representations using One-Hot Encoding.
- Scales numerical features using MinMaxScaler.
- Applies weighted Cosine Similarity to compare user preferences with restaurants.
- Returns the Top-N most similar restaurants.

The project follows a **content-based recommendation approach**.

---

## 🎯 Objectives

The main objectives of this project are:

1. Clean and preprocess the Swiggy restaurant dataset.
2. Handle missing and inconsistent values.
3. Convert categorical data into numerical features.
4. Scale numerical features appropriately.
5. Build a recommendation engine using Cosine Similarity.
6. Filter recommendations according to the selected city.
7. Provide an interactive Streamlit interface.
8. Test the recommendation system using different cities and cuisines.
9. Deploy the application for users to interact with.

---

## 📊 Dataset

The project uses a Swiggy restaurant dataset containing information about restaurants.

### Dataset Features

| Feature | Description |
|---|---|
| `id` | Unique restaurant identifier |
| `name` | Restaurant name |
| `city` | Restaurant location |
| `rating` | Restaurant rating |
| `rating_count` | Number of ratings |
| `cost` | Restaurant cost |
| `cuisine` | Cuisine offered |

The original dataset contains approximately **148,000+ restaurant records**.

After cleaning and preprocessing, the cleaned dataset is saved as:

```text
cleaned_data.csv

## Data Cleaning
The dataset contains missing values, inconsistent representations, and textual values in numerical columns.
Cleaning steps performed
* Removed duplicate records.
* Removed records where the restaurant name was missing.
* Converted rating values such as -- into missing values.
* Converted rating values to numerical format.
* Converted rating count categories into numerical values.
* Removed the ₹ symbol and commas from cost values.
* Converted cost values into numerical format.
* Filled missing numerical values using the median.
* Filled missing cuisine values with Unknown.
* Removed unrealistic or invalid cost values.

## Exploratory Data Analysis

Exploratory analysis was performed to understand the restaurant dataset.

The dataset contains approximately:

821 unique cities
2,133 unique cuisine combinations
Popular cities

Some cities/locations with a high number of restaurant records include:

Bikaner
Noida-1
Indirapuram,Delhi
BTM,Bangalore
Rohini,Delhi
Kothrud,Pune
Indiranagar,Bangalore
Electronic City,Bangalore
Popular cuisines

Frequently occurring cuisines include:

North Indian,Chinese
Indian
Chinese
North Indian
Indian,Chinese
South Indian
Bakery
Biryani
Pizzas
Beverages

EDA helped identify the distribution of restaurants across cities and cuisines and guided the preprocessing and recommendation approach.

## One-Hot Encoding

Categorical features cannot be directly used in numerical similarity calculations.

Therefore, One-Hot Encoding is applied to:

city
cuisine

Feature Scaling

Numerical features have different ranges.

For example:

Rating       → approximately 1–5
Rating Count → tens to thousands
Cost         → tens to thousands

Therefore, MinMaxScaler is used to normalize the numerical features.

The fitted scaler is saved as:

scaler.pkl

Scaling prevents features with larger numerical ranges from dominating the similarity calculation.

Recommendation Pipeline

The overall recommendation workflow is:

                 Swiggy Dataset
                       │
                       ▼
                Data Cleaning
                       │
                       ▼
                cleaned_data.csv
                       │
                       ▼
              One-Hot Encoding
                       │
                       ▼
              Feature Scaling
                       │
                       ├──────────────┐
                       ▼              ▼
                  encoder.pkl     scaler.pkl
                       │              │
                       └──────┬───────┘
                              ▼
                    Recommendation Engine
                              │
                              ▼
                       City Filtering
                              │
                              ▼
                  Weighted Cosine Similarity
                              │
                              ▼
                         Top-N Results
                              │
                              ▼
                        Streamlit App

## Streamlit Application

The project includes an interactive Streamlit web application.

The application allows users to select:

📍 City
🍛 Cuisine
⭐ Preferred Rating
👍 Preferred Rating Count
💰 Preferred Cost
🔢 Number of Recommendations

After clicking:

Get Restaurant Recommendations

the recommendation engine returns the most similar restaurants.

## Limitations

The current recommendation system has some limitations:

Recommendations depend on the available restaurant data.
The system does not use user history or previous interactions.
It does not currently provide personalized recommendations based on multiple users.
Cuisine values are treated as categorical combinations.
The system uses predefined feature weights.
Restaurants with identical feature values can receive very similar similarity scores.
Recommendation quality depends on the quality and completeness of the dataset.

## Future Enhancements

The system can be improved by adding:

User-based recommendation history.
Collaborative filtering.
Hybrid recommendation techniques.
More detailed cuisine processing.
Distance-based recommendations.
Restaurant location mapping.
Price-range filtering.
Personalized recommendations.
Restaurant popularity analysis.
Advanced ranking techniques.
Recommendation diversity controls.
User feedback to improve future recommendations.

## Conclusion

The Swiggy Restaurant Recommendation System demonstrates how machine learning and similarity-based techniques can be used to build a practical recommendation application.

## Live Streamlit Application:
https://swiggy-recommendation-system-qkh42re33qf7lgjdmuyhho.streamlit.app/
