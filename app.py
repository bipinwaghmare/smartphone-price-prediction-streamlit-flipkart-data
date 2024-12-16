import streamlit as st
import joblib
import numpy as np
import subprocess

# # Run master.py to trigger the end-to-end pipeline
# def run_master_pipeline():
#     try:
#         subprocess.run(["python", "src/master.py"], check=True)
#         st.success("Data pipeline executed successfully!")
#     except subprocess.CalledProcessError as e:
#         st.error(f"Pipeline execution failed: {e}")

# # Run the pipeline before launching the Streamlit app
# run_master_pipeline()


# Load the trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Load the label encoders
le_is_5G = joblib.load('is_5G_label_encoder.pkl')
le_storage_expandable = joblib.load('Storage_expandable_label_encoder.pkl')
le_display_type = joblib.load('Display_type_label_encoder.pkl')
le_processor_brand = joblib.load('Processor_brand_label_encoder.pkl')
le_product_brand = joblib.load('Product_brand_label_encoder.pkl')

# Streamlit interface
st.title('Mobile Price Prediction App')
st.write("This app predicts the price of a mobile phone based on its features.")

# Input fields
camera_details = st.text_input('Camera Details (Enter any number)')
rating = st.slider('Rating', 0.0, 5.0, 4.0)
warranty = st.slider('Warranty (Years)', 1, 3, 1)
is_5G = st.selectbox('Is it 5G?', ['Yes', 'No'])
storage_expandable = st.selectbox('Is Storage Expandable?', ['Yes', 'No'])
ram_in_gb = st.slider('RAM (GB)', 2, 12, 4)
rom_in_gb = st.slider('ROM (GB)', 32, 512, 64)
display_type = st.selectbox('Display Type', ['AMOLED', 'IPS', 'OLED', 'HD+ Display'])
display_size_in_inch = st.slider('Display Size (Inches)', 4.0, 7.0, 6.5)
rear_camera_in_mp = st.slider('Rear Camera (MP)', 5, 108, 50)
front_camera_in_mp = st.slider('Front Camera (MP)', 5, 32, 5)
battery_capacity_in_mah = st.slider('Battery Capacity (mAh)', 2000, 6000, 5000)
processor_brand = st.selectbox('Processor Brand', ['Mediatek', 'Qualcomm', 'Apple', 'Other'])
total_ratings = st.number_input('Total Ratings', 0, 1000000, 1000)
total_reviews = st.number_input('Total Reviews', 0, 100000, 1000)
product_brand = st.selectbox('Product Brand', ['POCO', 'Samsung', 'Apple', 'OnePlus', 'Realme', 'Other'])

# Encode categorical features
# encoded_is_5G = le_is_5G.transform([is_5G])[0]
# encoded_storage_expandable = le_storage_expandable.transform([storage_expandable])[0]
# encoded_display_type = le_display_type.transform([display_type])[0]
# encoded_processor_brand = le_processor_brand.transform([processor_brand])[0]
# encoded_product_brand = le_product_brand.transform([product_brand])[0]

def encode_feature(encoder, value, column_name):
    try:
        return encoder.transform([value])[0]
    except ValueError:
        st.warning(f"Unseen label '{value}' in {column_name}. Defaulting to -1.")
        return -1  # Assign default encoding for unseen labels

encoded_is_5G = encode_feature(le_is_5G, is_5G, 'is_5G')
encoded_storage_expandable = encode_feature(le_storage_expandable, storage_expandable, 'storage_expandable')
encoded_display_type = encode_feature(le_display_type, display_type, 'display_type')
encoded_processor_brand = encode_feature(le_processor_brand, processor_brand, 'processor_brand')
encoded_product_brand = encode_feature(le_product_brand, product_brand, 'product_brand')


# Prepare features
input_features = np.array([
    0, rating, warranty, encoded_is_5G, encoded_storage_expandable, 
    ram_in_gb, rom_in_gb, encoded_display_type, display_size_in_inch, 
    rear_camera_in_mp, front_camera_in_mp, battery_capacity_in_mah, 
    encoded_processor_brand, total_ratings, total_reviews, encoded_product_brand
]).reshape(1, -1)


st.write("Input features:", input_features)
print("Shape of input_features:", input_features.shape)
print("Scaler expected shape:", scaler.n_features_in_)


# Scale the features
# scaled_features = scaler.transform(input_features)

try:
    scaled_features = scaler.transform(input_features)
except Exception as e:
    st.error(f"Error scaling input features: {e}")

# Predict the price
if st.button('Predict Price'):
    prediction = model.predict(scaled_features)
    st.write(f"Predicted Price: ₹{prediction[0]:.2f}")
