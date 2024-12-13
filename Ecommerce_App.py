import streamlit as st
import pandas as pd

# Load your trained model
import joblib
model = joblib.load('random_forest_model.pkl')

# Step 4: Create a User Interface
# Create a title
st.title("Ad Spend Optimizer Prediction Model")

# Create a form
with st.form("my_form"):
    col1, col2 = st.columns(2)
    with col1:
        AOV = st.number_input("Average Order Value (AOV)")
        Ad_CPC = st.number_input("Ad_CPC")
        Ad_CTR = st.number_input("Ad_CTR")
        Ad_Spend = st.number_input("Amount Spent on Ad")
        Clicks = st.number_input("Number of Clicks")
        Conversion_Rate = st.number_input("Conversion Rate")
        Discount_Applied = st.number_input("Discount Applied")

    with col2: 
        Impressions = st.number_input("Impressions")
        Product_ID = st.number_input("Product ID")
        Category = st.number_input("Category")
        Region = st.number_input("Region")
        Revenue = st.number_input("Revenue")
        Units_Sold = st.number_input("Units Sold")

    submitted = st.form_submit_button("Predict")

# Make predictions when the form is submitted
if submitted:
    # Create a dictionary with the input values
    input_data = { 'AOV': AOV, 'Ad_CPC': Ad_CPC, 'Ad_CTR': Ad_CTR, 'Ad_Spend': Ad_Spend, 'Clicks': Clicks, 
                    'Conversion_Rate': Conversion_Rate, 'Discount_Applied': Discount_Applied, 'Impressions': Impressions, 
                    'Product_ID': Product_ID, 'Category': Category, 'Region': Region, 'Revenue': Revenue, 'Units_Sold': Units_Sold}
    # Make a prediction using your model
    prediction = model.predict(pd.DataFrame([input_data]))
    # Display the prediction
    st.write("Prediction:", prediction)
