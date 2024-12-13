import streamlit as st
import pandas as pd

# Load your trained model
import joblib
model = joblib.load('random_forest_model.pkl')

# Converting of Encoded values on categorical variables back to the original values 
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Step 1: Prepare the data and encoders
categories = ["Electronics", "Home Appliances", "Toys", "Clothing", "Books"]
regions = ["North America", "Asia", "Europe"]

# Create LabelEncoders for categories and regions
category_encoder = LabelEncoder()
region_encoder = LabelEncoder()

# Fit encoders
category_encoded = category_encoder.fit_transform(categories)
region_encoded = region_encoder.fit_transform(regions)

# Create mappings
category_mapping = dict(zip(categories, category_encoded))
region_mapping = dict(zip(regions, region_encoded))



# Step 4: Create a User Interface
# Create a title
st.title("Ad Spend Optimizer Prediction Model")

# Create a form
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
        selected_category = st.selectbox("Select a category:", categories)
        selected_region = st.selectbox("Select a region:", regions)
        encoded_category = category_mapping[selected_category]
        encoded_region = region_mapping[selected_region]        
        Revenue = st.number_input("Revenue")
        Units_Sold = st.number_input("Units Sold")


# Make predictions when the form is submitted
if st.button("Predict"):
    # Create a dictionary with the input values
    input_data = { 'AOV': AOV, 'Ad_CPC': Ad_CPC, 'Ad_CTR': Ad_CTR, 'Ad_Spend': Ad_Spend, 'Clicks': Clicks, 
                    'Conversion_Rate': Conversion_Rate, 'Discount_Applied': Discount_Applied, 'Impressions': Impressions, 
                    'Product_ID': Product_ID, 'Category': encoded_category, 'Region': encoded_region, 'Revenue': Revenue, 'Units_Sold': Units_Sold}
    # Make a prediction using your model
    prediction = model.predict(pd.DataFrame([input_data]))
    # Display the prediction
    st.write("Prediction:", prediction)
