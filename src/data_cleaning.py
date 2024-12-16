import pandas as pd
import numpy as np
import os
import re

df = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\combined_df.csv")

df['Price'] = df['Price'].str.replace('₹', '')
df['Price'] = df['Price'].str.replace(',', '')

df['Product_name'] = df['Product_name'].str.replace(r"\s*\(.*?\)", "", regex=True)

df['is_5G'] = df['Product_name'].apply(lambda x: 'Yes' if '5G' in x else 'No')

df['Storage_expandable'] = df['Storage'].apply(lambda x: 'Yes' if 'Expandable' or 'expandable' in x else 'No')

# Function to extract RAM
def extract_ram(storage):
    match = re.search(r'\d+\s?GB RAM', storage)
    return match.group(0) if match else "Not Available"

# Function to extract ROM
def extract_rom(storage):
    match = re.search(r'\d+\s?GB ROM', storage)
    return match.group(0) if match else "Not Available"

df['RAM_in_GB'] = df['Storage'].apply(extract_ram)
df['ROM_in_GB'] = df['Storage'].apply(extract_rom)

df = df.drop(['Storage'], axis=1)

# Function to extract display type (after the parenthesis)
def extract_display_type(Display_size):
    match = re.search(r'\)\s*(.+)', Display_size)  # Matches anything after ') '
    return match.group(1).strip() if match else "Not Available"

# Function to extract display size (inside the parenthesis)
def extract_display_size(Display_size):
    match = re.search(r'\(([^)]+)\)', Display_size)  # Matches anything inside '( )'
    return match.group(1).strip() if match else "Not Available"

# Apply the functions to the 'Display_size' column
df['Display_type'] = df['Display_size'].apply(extract_display_type)
df['Display_size_in_inch'] = df['Display_size'].apply(extract_display_size)

df.drop('Display_size',axis = 1, inplace = True)

# Function to extract the highest MP value from the rear camera
def extract_rear_camera(camera_details):
    rear_part = camera_details.split('|')[0].strip()  # Get the rear camera part
    matches = re.findall(r'\d+', rear_part)          # Find all numbers in the rear part
    return max(map(int, matches)) if matches else None  # Return the highest MP or None

# Function to extract the MP value for the front camera
def extract_front_camera(camera_details):
    front_part = camera_details.split('|')[-1].strip()  # Get the front camera part
    matches = re.findall(r'\d+', front_part)           # Find all numbers in the front part
    return max(map(int, matches)) if matches else None  # Return the highest MP or None

# Apply the functions to the 'Camera Details' column
df['Rear_camera_in_MP'] = df['Camera Details'].apply(extract_rear_camera)
df['Front_camera_in_MP'] = df['Camera Details'].apply(extract_front_camera)

def extract_battery_capacity(battery):
    match = re.search(r'(\d+)\s?mAh', battery)
    return match.group(1) if match else "Not Available"

df['Battery_capacity_in_mAh'] = df['Battery'].apply(extract_battery_capacity)

df.drop('Battery', axis = 1, inplace = True)

df['Warranty'] = df['Warranty'].str.replace('years', 'Year')

# Function to classify processor brand
def classify_processor(processor):
    if 'Qualcomm' in processor or 'Gen' in processor or 'Snapdragon' in processor.lower():
        return 'Snapdragon'
    elif 'Helio' in processor or 'Mediatek Helio' in processor or 'helio' in processor.lower():
        return 'Mediatek Helio'
    elif 'Dimensity' in processor or 'Mediatek Dimensity' in processor or 'dimensity' in processor.lower():
        return 'Mediatek Dimensity'
    elif 'Unisoc' in processor or 'T612' in processor:
        return 'Unisoc'
    else:
        return 'Other'

# Apply the function to create the new column
df['Processor_brand'] = df['Processor'].apply(classify_processor)



# Function to extract ratings and reviews
def extract_ratings_and_reviews(review):
    # Remove commas first
    cleaned_review = review.replace(',', '')

    # Extract ratings and reviews from cleaned string
    ratings_match = re.search(r'(\d+)\s?Ratings', cleaned_review)
    reviews_match = re.search(r'(\d+)\s?Reviews', cleaned_review)

    if not ratings_match or not reviews_match:
        return "Not Available", "Not Available"

    ratings = ratings_match.group(1) if ratings_match else "Not Available"
    reviews = reviews_match.group(1) if reviews_match else "Not Available"

    return int(ratings), int(reviews)

df[['Total_Ratings', 'Total_Reviews']] = df['Overall_Review'].apply(lambda x: pd.Series(extract_ratings_and_reviews(x)))

df.drop(['Processor','Overall_Review'], axis = 1, inplace = True)

def update_warranty(warranty):
    # Check for conditions and return the corresponding value
    if '1' in warranty or '12' in warranty:
        return 1
    elif '2' in warranty or '24' in warranty:
        return 2
    else:
        return 'Not Available'

# Apply the function to the 'Warranty' column
df['Warranty'] = df['Warranty'].apply(update_warranty)

df['product_brand'] = df['Product_name'].apply(lambda x: x.split()[0])

df['RAM_in_GB'] = df['RAM_in_GB'].apply(lambda x: x.split()[0])

df['ROM_in_GB'] = df['ROM_in_GB'].apply(lambda x: x.split()[0])

df['Display_size_in_inch'] = df['Display_size_in_inch'].apply(lambda x: x.split()[0])

# Replace 'Not Available' with NaN
df.replace(['Not Available', 'Not'], np.nan, inplace=True)

# Convert columns to appropriate data types
# Convert numeric columns (Price, Total_Ratings, Total_Reviews, etc.)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Total_Ratings'] = pd.to_numeric(df['Total_Ratings'], errors='coerce')
df['Total_Reviews'] = pd.to_numeric(df['Total_Reviews'], errors='coerce')
df['Display_size_in_inch'] = pd.to_numeric(df['Display_size_in_inch'], errors='coerce')
df['Battery_capacity_in_mAh'] = pd.to_numeric(df['Battery_capacity_in_mAh'], errors='coerce')
df['Rear_camera_in_MP'] = pd.to_numeric(df['Rear_camera_in_MP'], errors='coerce')
df['Front_camera_in_MP'] = pd.to_numeric(df['Front_camera_in_MP'], errors='coerce')


# Convert 'RAM_in_GB' and 'ROM_in_GB' to numeric (if applicable)
df['RAM_in_GB'] = df['RAM_in_GB'].apply(lambda x: str(x).split()[0]).astype(float)
df['ROM_in_GB'] = df['ROM_in_GB'].apply(lambda x: str(x).split()[0]).astype(float)

# For warranty, you can convert the column similarly (if necessary)
df['Warranty'] = pd.to_numeric(df['Warranty'], errors='coerce')

df.dropna(inplace = True)

folder = r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data'

df.to_csv(os.path.join(folder, 'df.csv'), index=False)



