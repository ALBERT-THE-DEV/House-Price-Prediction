# House-Price-Prediction (Linear Regression)

This project predicts house prices using a Linear Regression model. The app is deployed using Streamlit and allows users to input various house features to get an estimated cost.

Project Overview
----------------
The dataset is a synthetic dataset of 600 house records with features such as area, bedrooms, bathrooms, stories, and other housing features. Price tiers are categorized as Economy (below 500,000), Midscale (500,000–1,000,000), and Luxury (above 1,000,000). The model used is Linear Regression trained on the dataset with categorical features encoded using label encoders.

Features Used
-------------
Numeric features: Area, Bedrooms, Bathrooms, Stories, and Parking. 

Categorical features: Main road access, Guest room, Basement, Hot water heating, Air conditioning, Preferred area, and Furnishing status.

How to Use
----------
1. Clone the repository.
2. Install the required packages using the command: pip install -r requirements.txt
3. Run the Streamlit app using the command: streamlit run streamlit_app.py
4. Input the house details in the web interface to get the predicted price.

Files in Repository
-------------------
- streamlit_app.py: Streamlit web application
- linear_regression_large_housing_model.joblib: Joblib file containing trained model
- label_encoders.pkl: Encoders for categorical features
- housing_large_dataset.csv: Dataset used for training the model
- model_training.py: Script used to train the Linear Regression model
- requirements.txt: Python packages required to be installed

Model Details
--------------
The model predicts house prices using the linear equation:

Price = β0 + β1*(Area) + β2*(Bedrooms) + β3*(Bathrooms) + ... + βn*(Feature_n)

, where each β represents the learned weight for that feature.

Feature Importance Analysis
---------------------------
After training, the following features were found to have the most significant influence on the predicted house prices based on model coefficients:

Feature | Influence | Description
Bathrooms | Strong positive | More bathrooms significantly increase price.
Furnishing Status | Moderate positive | Furnished and semi-furnished houses tend to cost more.
Basement | Moderate positive | Houses with basements have higher value.
Guestroom | Mild positive | Presence of a guestroom adds to the price.
Area | Mild positive | Larger floor area increases price proportionally.
Bedrooms, Prefarea, Stories | Weak or negative | These features showed less or inverse correlation due to dataset structure.

The model’s coefficients indicate that interior and comfort-based features (bathrooms, furnishing, and basement) have the strongest effect on price, while size (area) also contributes significantly.

Deployment
----------
The app is deployed online using Streamlit Cloud and can be accessed at: https://house-price-prediction-6tai5qkqgam6ge2ykk4rj8.streamlit.app

The model can also be run locally using the instructions above.

Model Performance
-----------------
During the training phase, the Linear Regression model achieved an R² score of 1.0 and an RMSE of approximately 10,615 on a synthetic dataset consisting of 600 samples. On an external house dataset consisting of 15 samples that was not used in training, the model achieved an R² score of 0.431 and an RMSE of approximately 106,696. These metrics show that the model fits the training data well and provides reasonable predictions on unseen houses, demonstrating its generalization ability.



