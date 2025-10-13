import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib

#Load the dataset
df = pd.read_csv("housing_large_dataset.csv")

#Encode categorical features
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creating model using Linear Regression & fit the dataset 
model = LinearRegression()
model.fit(X_train, y_train)

#Evaluating the model's prediction performance
y_pred = model.predict(X_test)
print("\nModel Performance:")
print(f"R² Score: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")

#Saving the trained model
joblib.dump(model, "linear_regression_large_housing_model.joblib")

#Predicting new house prices
print("\nEnter house details to predict price:")

user_input = {}
for col in X.columns:
    if col in label_encoders:  
        options = list(label_encoders[col].classes_)
        val = input(f"Enter {col} ({'/'.join(options)}): ").strip()
        matched_val = next((opt for opt in options if opt.lower() == val.lower()), options[0])
        encoded_val = label_encoders[col].transform([matched_val])[0]
        user_input[col] = encoded_val
    else:  
        while True:
            try:
                val = float(input(f"Enter {col}: "))
                user_input[col] = val
                break
            except ValueError:
                print("Please enter a valid number.")

input_df = pd.DataFrame([user_input])
predicted_price = model.predict(input_df)[0]
print(f"\nPredicted House Price: {predicted_price:,.0f}")

