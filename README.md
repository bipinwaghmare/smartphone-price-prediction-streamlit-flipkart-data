# Smartphone Price Prediction App using Streamlit and Scraped Flipkart Data

## Overview
This project is an end-to-end pipeline for predicting the price of smartphones using **scraped data from Flipkart**. The data, originally containing around **2000 rows and 10 columns**, was cleaned and enhanced through **EDA**, **data cleaning**, and **feature engineering**, resulting in **16 columns** with slightly fewer rows. The project includes:
- **Data Collection**: Scraping smartphone data from Flipkart.
- **Data Cleaning and Preprocessing**: Transforming raw data into a structured format with additional engineered features.
- **Model Building**: Training a machine learning model to predict smartphone prices.
- **Streamlit App**: An interactive web application for making predictions based on smartphone features.

---

## Features
1. **Data Pipeline**:
   - Combine multiple scraped CSV files into one dataset.
   - Clean and preprocess data, handling missing values, outliers, and encoding categorical features.
   - Perform feature engineering to extract meaningful insights (e.g., RAM, ROM, processor type, camera specifications, etc.).
2. **Model**:
   - Train a **Gradient Boosting Regressor** for price prediction.
3. **Interactive Web App**:
   - Users can input smartphone specifications to predict prices dynamically.

---

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: 
  - Web Scraping: `pandas`, `numpy`
  - Machine Learning: `sklearn`, `joblib`
  - Web Application: `streamlit`
- **Model**: Gradient Boosting Regressor
- **Platform**: Flipkart (Data Source)

---

## Dataset
- **Original Data**: ~2000 rows and 10 columns.
- **Transformed Data**:
  - **Rows**: Slightly reduced due to data cleaning.
  - **Columns**: Increased to 16 after feature engineering, including:
    - `RAM_in_GB`, `ROM_in_GB`, `Rear_camera_in_MP`, `Front_camera_in_MP`
    - `Battery_capacity_in_mAh`, `is_5G`, `Storage_expandable`
    - `Processor_brand`, `Display_type`, `Display_size_in_inch`
    - `Rating`, `Warranty`, `Total_Ratings`, `Total_Reviews`, `product_brand`, and `Price`.

---

## Folder Structure
```
project/
│
├── data/
│   ├── raw_data/             # Raw scraped data (2000 rows, 10 columns)
│   ├── clean_data/           # Preprocessed and feature-engineered data (16 columns)
│
├── src/
│   ├── data_collection.py    # Combines raw scraped data
│   ├── data_cleaning.py      # Cleans and preprocesses data
│   ├── preprocessing.py      # Encodes and scales data
│   ├── model_building.py     # Trains the model
│   ├── model_evaluation.py   # Evaluates the model
│
├── app.py                    # Streamlit web app (outside the src folder)
├── combined_file.csv         # Final combined dataset
├── model.pkl                 # Trained Gradient Boosting Regressor model
├── scaler.pkl                # Scaler for feature transformation
├── README.md                 # Project description
```

---

## How to Run the Project

### Prerequisites
1. Python 3.x installed.
2. Required libraries:
   ```bash
   pip install pandas numpy sklearn streamlit joblib
   ```

### Steps to Execute
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/smartphone-price-prediction-streamlit-flipkart-data.git
   cd smartphone-price-prediction-streamlit-flipkart-data
   ```
2. **Run the Pipeline**:
   - Execute all preprocessing steps by running `master.py`:
     ```bash
     python src/master.py
     ```
   - This combines raw data, cleans it, preprocesses it, and trains the model.
3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```
4. **Use the App**:
   - Open the link provided by Streamlit in your browser.
   - Input smartphone specifications to get price predictions.

---

## Example Workflow
1. **Input Features**:
   - Camera Details
   - RAM, ROM
   - Battery Capacity
   - Display Type, Processor Brand
   - Whether 5G is supported or storage is expandable
2. **Predicted Output**:
   - Smartphone price in INR (₹).

---

## Model Performance
- **Current Model**: Gradient Boosting Regressor
- **Evaluation Metrics**:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
- **Note**: Model performance will improve as more data is added.

---

## Future Work
- Add more scraped data to improve model accuracy.
- Experiment with advanced models like XGBoost or Neural Networks.
- Refine feature engineering and outlier detection.
- Enhance the app's UI/UX for better user interaction.

---

## Acknowledgments
- Data Source: Flipkart
- Tools: Streamlit, Scikit-learn, Python

---

## License
This project is open-source under the MIT License.
