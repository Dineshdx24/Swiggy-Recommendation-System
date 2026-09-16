# Swiggy-Recommendation-System

# Introduction
Explain the purpose of the project and why restaurant recommendation is useful.
# Problem Statement
Describe the problem of helping users find restaurants according to their preferences.
# Objectives
* Recommend restaurants based on user preferences.
* Consider city, cuisine, rating, rating count, and cost.
* Clean and preprocess the Swiggy dataset.
* Build a similarity-based recommendation engine.
* Develop an interactive Streamlit application.
# Limitations
* Recommendations depend on the information available in the dataset.
* rating_count is treated as a preference rather than a strict minimum.
* The system does not use restaurant menu-level information because your working dataset contains the selected seven columns.
* The system does not currently incorporate user history or personalized behavior.
* Cosine similarity measures feature similarity; it does not understand actual user reviews or sentiment.
# Future Enhancements
* Add restaurant menu information.
* Incorporate user ratings and historical interactions.
* Add review sentiment analysis.
* Develop personalized recommendations based on previous selections.
* Add location/distance-based recommendations.
* Experiment with other recommendation algorithms.
* Add restaurant links/details to the Streamlit interface.
