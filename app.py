# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("Logistic Regression Prediction App")

st.write("""
### Enter the details below to get a prediction
""")

# Assuming you have 4 features (update according to your model!)
feature1 = st.number_input('Feature 1', min_value=0.0, max_value=1000.0, value=0.0)
feature2 = st.number_input('Feature 2', min_value=0.0, max_value=1000.0, value=0.0)
feature3 = st.number_input('Feature 3', min_value=0.0, max_value=1000.0, value=0.0)
feature4 = st.number_input('Feature 4', min_value=0.0, max_value=1000.0, value=0.0)

# Prepare input data
input_data = np.array([[feature1, feature2, feature3, feature4]])

# Predict button
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.success(f'The prediction is: {prediction[0]}')

