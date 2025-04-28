import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# App Title
st.title("Sales Prediction App")

st.header("Input the feature values:")

# Input fields for each feature
Category_Electronics = st.selectbox('Is the Category Electronics?', [0, 1])
Category_Furniture = st.selectbox('Is the Category Furniture?', [0, 1])
Region_South = st.selectbox('Is the Region South?', [0, 1])
Region_West = st.selectbox('Is the Region West?', [0, 1])
Weather_Rainy = st.selectbox('Is the Weather Rainy?', [0, 1])
Weather_Sunny = st.selectbox('Is the Weather Sunny?', [0, 1])
Seasonality_Summer = st.selectbox('Is the Seasonality Summer?', [0, 1])

Inventory = st.number_input('Enter Inventory value')
Revenue = st.number_input('Enter Revenue value')
Sales = st.number_input('Enter Sales value')

# Predict button
if st.button('Predict'):
    # Prepare input in the correct order
    input_data = np.array([[Category_Electronics, Category_Furniture, Region_South,
                            Region_West, Weather_Rainy, Weather_Sunny, Seasonality_Summer,
                            Inventory, Revenue, Sales]])
    
    # Prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.success(f"The predicted value is: {prediction[0]:.2f}")

# Footer
st.markdown("""
    <hr>
    <small>Developed with ❤️ using Streamlit</small>
""", unsafe_allow_html=True)
