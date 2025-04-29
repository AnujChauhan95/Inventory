import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

st.title("Petroleum Revenue Prediction App")

st.header("Enter Feature Values")

# Input fields for categorical features
land_class = st.selectbox("Land Class", ['Federal', 'Private', 'State'])  # Example options
land_category = st.selectbox("Land Category", ['Onshore', 'Offshore'])
state = st.selectbox("State", ['Texas', 'Alaska', 'California'])  # Add actual state list
revenue_type = st.selectbox("Revenue Type", ['Royalty', 'Bonus', 'Rent'])
lease_type = st.selectbox("Mineral Lease Type", ['Competitive', 'Non-Competitive'])
commodity = st.selectbox("Commodity", ['Oil', 'Gas', 'Coal'])
county = st.selectbox("County", ['County A', 'County B', 'County C'])  # Replace with real counties
product = st.selectbox("Product", ['Crude Oil', 'Natural Gas', 'NGL'])  # Example options

# Build input DataFrame
input_dict = {
    'Land Class': land_class,
    'Land Category': land_category,
    'State': state,
    'Revenue Type': revenue_type,
    'Mineral Lease Type': lease_type,
    'Commodity': commodity,
    'County': county,
    'Product': product
}
input_df = pd.DataFrame([input_dict])

# Dummy prediction function
def dummy_model_predict(df):
    # Encode categorical variables
    for col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    
    # Dummy model (you will replace this with a real trained model)
    model = RandomForestRegressor()
    model.fit(X_scaled, [100000])  # Dummy target
    prediction = model.predict(X_scaled)
    return prediction[0]

# Prediction
if st.button("Predict Revenue"):
    prediction = dummy_model_predict(input_df)
    st.success(f"Estimated Revenue: ${prediction:,.2f}")

st.markdown("""
<hr>
<small>Developed with ❤️ using Streamlit</small>
""", unsafe_allow_html=True)
