# House-Price-Prediction
House Price Prediction Web App

This project predicts house prices using a Linear Regression model. The app is deployed using Streamlit and allows users to input various house features to get an estimated price.

Project Overview

The dataset is a synthetic dataset of 600 house records with features such as area, bedrooms, bathrooms, stories, and amenities. Price tiers are categorized as Low (below 500,000), Mid (500,000–1,000,000), and High (above 1,000,000). The model used is Linear Regression trained on the dataset with categorical features encoded using label encoders.

Features Used

Numeric features include Area, Bedrooms, Bathrooms, Stories, and Parking. Categorical features include Main road access, Guest room, Basement, Hot water heating, Air conditioning, Preferred area, and Furnishing status.

How to Use

1. Clone the repository.
2. Install the required packages using the command: pip install -r requirements.txt
3. Run the Streamlit app using the command: streamlit run app.py
4. Input the house details in the web interface to get the predicted price.

Files in Repository

- app.py : Streamlit web application
- linear_regression_large_housing_model.joblib : Trained model
- label_encoders.pkl : Encoders for categorical features
- housing_large_dataset.csv : Dataset used for training
- model_training.py : Script used to train the Linear Regression model
- requirements.txt : Python packages required

Model Details

The model predicts house price using the linear equation:

Price = β0 + β1*(Area) + β2*(Bedrooms) + β3*(Bathrooms) + ... + βn*(Feature_n)

where each β represents the learned weight for that feature.

Deployment

The app is deployed online using Streamlit Cloud and can be accessed at: [Live Streamlit App URL]

The model can also be run locally using the instructions above.

License

This project is for educational purposes and can be freely used for demonstration.
