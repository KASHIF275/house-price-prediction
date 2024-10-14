import streamlit as st
import joblib
import numpy as np

# Save kiya hua model load karte hain
model = joblib.load('house.joblib')

# Streamlit app ka title
st.title("House Price Prediction App")

# User input le lo
area = st.number_input("Enter area of the house (in sqft)", min_value=0)
bhk = st.number_input("Enter number of bedrooms (BHK)", min_value=0)
bathroom = st.number_input("Enter number of bathrooms", min_value=0)

# Predict button
if st.button("Predict Price per Sqft"):
    # User ke input se prediction karte hain
    input_features = np.array([[area, bhk, bathroom]])
    prediction = model.predict(input_features)
    st.write(f"The predicted price per square foot is ${prediction[0]:,.2f}")
