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
Category_Electronics = int(st.selectbox('Is the Category Electronics?', [0, 1]))
Category_Furniture = int(st.selectbox('Is the Category Furniture?', [0, 1]))
Region_South = int(st.selectbox('Is the Region South?', [0, 1]))
Region_West = int(st.selectbox('Is the Region West?', [0, 1]))
Weather_Rainy = int(st.selectbox('Is the Weather Rainy?', [0, 1]))
Weather_Sunny = int(st.selectbox('Is the Weather Sunny?', [0, 1]))
Seasonality_Summer = int(st.selectbox('Is the Seasonality Summer?', [0, 1]))
Seasonality_Winter = int(st.selectbox('Is the Seasonality Winter?', [0, 1]))
Promotion_True = int(st.selectbox('Is the Promotion True?', [0, 1]))


Inventory = st.number_input('Enter Inventory value', min_value=0.0)
Price = st.number_input('Enter Price value', min_value=0.0)
Revenue = st.number_input('Enter Revenue value', min_value=0.0)
Sales = st.number_input('Enter Sales value', min_value=0.0)
Competitor_Pricing = st.number_input('Enter Competitor_Pricing value', min_value=0.0)
Orders = st.number_input('Enter Orders value', min_value=0.0)
Discount = st.number_input('Enter Discount value', min_value=0.0)
 

# Prediction
if st.button('Predict'):
    input_data = np.array([['Weather_Rainy', 'Region_South', 'Revenue', 'Sales',
       'Seasonality_Winter', 'Region_West', 'Weather_Sunny', 'Promotion_True',
       'Seasonality_Summer', 'Competitor_Pricing', 'Orders', 'Discount',
       'Inventory', 'Category_Electronics', 'Price', 'Category_Furniture']])
    
    prediction = model.predict(input_data)
    st.success(f"The predicted value is: {prediction[0]:.2f}")

# Footer
st.markdown("""
    <hr>
    <small>Developed with ❤️ using Streamlit</small>
""", unsafe_allow_html=True)
