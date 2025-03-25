import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Set page title
st.title('Gender Prediction from Height and Shoe Size')

# Load the saved model
@st.cache_resource  # This caches the model to avoid reloading it every time
def load_model():
    return joblib.load('naive_bayes_gender_model_US.pkl')

model = load_model()

# Create input fields
st.subheader('Enter Physical Measurements')

# User inputs - US format (feet and inches)
col1, col2 = st.columns(2)
with col1:
    feet = st.number_input('Height (feet)', min_value=1, max_value=8, value=5, step=1)
with col2:
    inches = st.number_input('Height (inches)', min_value=0, max_value=11, value=6, step=1)

# Calculate total height in feet (as decimal) for the model
height = feet + (inches / 12)

normalized_shoe_size = st.number_input('Shoe Size (US)', min_value=1.0, max_value=20.0, value=9.0, step=0.5)

# When the 'Predict' button is clicked
if st.button('Predict Gender'):
    
    # Create a dataframe with the input values
    input_data = pd.DataFrame({
        'height': [height],
        'normalized_shoe_size': [normalized_shoe_size]  # Using the feature name from the model
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    # Display result
    st.subheader('Prediction Result')
    
    # Display the height used for prediction
    st.write(f'Height used for prediction: **{height:.2f} ft** (from {feet}\' {inches}")')
    st.write(f'Shoe size used for prediction: **{normalized_shoe_size}** (US)')
    
    if prediction == 1:
        st.write(f'Predicted Gender: **Man**')
        st.write(f'Probability: **{probability[1]:.2%}**')
    else:
        st.write(f'Predicted Gender: **Woman**')
        st.write(f'Probability: **{probability[0]:.2%}**')
    
    # Visualize the prediction with a gauge or bar
    st.subheader('Probability Distribution')
    st.bar_chart(pd.DataFrame({
        'Woman': [probability[0]],
        'Man': [probability[1]]
    }).T)
