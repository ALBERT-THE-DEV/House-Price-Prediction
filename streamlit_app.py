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


st.divider()
st.subheader("About the Model")

st.markdown("""
This prediction model is built using **Linear Regression**, a fundamental machine learning algorithm for continuous data.
It was trained on **600 synthetic housing records** categorized into:
- Low-tier houses (below 500K)
- Mid-tier houses (500K – 1M)
- High-tier houses (above 1M)

The model learns relationships between key features such as:
- Area, Bedrooms, Bathrooms, Stories
- Main Road, Air Conditioning, Basement, Furnishing Status, etc.

The result is a simple yet effective regression model capable of estimating house prices with realistic variance across property types.
""")

with st.expander("Model's Working based Formula"):
    st.markdown(r"""
    The price is predicted using the equation:

    \[
    \text{Price} = \beta_0 + \beta_1(\text{Area}) + \beta_2(\text{Bedrooms}) + \beta_3(\text{Bathrooms}) + \dots + \beta_n(\text{Feature}_n)
    \]

    where each β represents the learned coefficient that determines how much that feature affects the overall price.
    """)

   

