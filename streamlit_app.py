import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load("linear_regression_large_housing_model.joblib")

# Load label encoders
import pickle
with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

st.title("House Price Predictor")

st.markdown("Enter house details below to predict the house price.")

# Housing detail Inputs
area = st.number_input("Area (sq ft):", min_value=0, placeholder="Enter the area")
bedrooms = st.number_input("Bedrooms:", min_value=0, placeholder="Enter the number of bedrooms")
bathrooms = st.number_input("Bathrooms:", min_value=0, placeholder="Enter the number of bathrooms")
stories = st.number_input("Stories:", min_value=0, placeholder="Enter the number of floor levels")
mainroad = st.selectbox("Main Road (yes/no):", ["yes","no"])
guestroom = st.selectbox("Guest Room (yes/no):", ["yes","no"])
basement = st.selectbox("Basement (yes/no):", ["yes","no"])
hotwaterheating = st.selectbox("Hot Water Heating (yes/no):", ["yes","no"])
airconditioning = st.selectbox("Air Conditioning (yes/no):", ["yes","no"])
parking = st.number_input("Parking:", min_value=0, placeholder="Enter the number of parking lots")
prefarea = st.selectbox("Preferred Area (yes/no):", ["yes","no"])
furnishingstatus = st.selectbox("Furnishing Status:", ["furnished","semi-furnished","unfurnished"])

# Save details to DataFrame 
input_dict = {
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "mainroad": mainroad,
    "guestroom": guestroom,
    "basement": basement,
    "hotwaterheating": hotwaterheating,
    "airconditioning": airconditioning,
    "parking": parking,
    "prefarea": prefarea,
    "furnishingstatus": furnishingstatus
}
input_df = pd.DataFrame([input_dict])

# Encoding categorical features
for col in input_df.select_dtypes(include='object').columns:
    le = label_encoders[col]
    input_df[col] = le.transform(input_df[col])

if st.button("Predict House Price", help="Click to estimate the house price.", type="primary"):
    price = model.predict(input_df)[0]
    st.success(f"Predicted House Price: {price:,.0f}")

    # Housing economy classification
    if price < 500000:
        tier = "Economy"
    elif price <= 1000000:
        tier = "Midscale"
    else:
        tier = "Luxury"
    st.info(f"Price Tier: {tier}")

   
