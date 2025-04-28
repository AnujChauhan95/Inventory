import streamlit as st
import pickle
import numpy as np

# Load the model correctly
with open('model.pkl', 'rb') as file:
    model_data = pickle.load(file)
    model = model_data['model']  # extract 'model' from dict

# App Title
st.title("Sales Prediction App")

st.header("Input the feature values:")

# Input fields
Category_Electronics = st.selectbox('Is the Category Electronics?', [0, 1])
Category_Furniture = st.selectbox('Is the Category Furniture?', [0, 1])
Region_South = st.selectbox('Is the Region South?', [0, 1])
Region_West = st.selectbox('Is the Region West?', [0, 1])
Weather_Rainy = st.selectbox('Is the Weather Rainy?', [0, 1])
Weather_Sunny = st.selectbox('Is the Weather Sunny?', [0, 1])
Seasonality_Summer = st.selectbox('Is the Seasonality Summer?', [0, 1])

Inventory = st.number_input('Enter Inventory value', min_value=0.0)
Revenue = st.number_input('Enter Revenue value', min_value=0.0)
Sales = st.number_input('Enter Sales value', min_value=0.0)

# Prediction
if st.button('Predict'):
    input_data = np.array([[Category_Electronics, Category_Furniture, Region_South,
                            Region_West, Weather_Rainy, Weather_Sunny, Seasonality_Summer,
                            Inventory, Revenue, Sales]])
    
    prediction = model.predict(input_data)
    st.success(f"The predicted value is: {prediction[0]:.2f}")

# Footer
st.markdown("""
    <hr>
    <small>Developed with ❤️ using Streamlit</small>
""", unsafe_allow_html=True)
