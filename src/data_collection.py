import pandas as pd
import numpy as np
import os

# Combining the files.

# List of CSV file paths
"""csv_files = ['/content/drive/MyDrive/DL/flipkart/flipkart_mobile_data.csv', '/content/drive/MyDrive/DL/flipkart/flipkart_mobile_data_1.csv',
             '/content/drive/MyDrive/DL/flipkart/flipkart_mobile_data_2.csv', '/content/drive/MyDrive/DL/flipkart/flipkart_mobile_data_3.csv',
             '/content/drive/MyDrive/DL/flipkart/flipkart_mobile_data_4.csv', '/content/drive/MyDrive/DL/flipkart/flipkart_mobile_data_5.csv',
             '/content/drive/MyDrive/DL/flipkart/flipkart_mobile_data_6.csv']  # Replace with your file names"""

csv_files = [r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\flipkart_mobile_data.csv', r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\flipkart_mobile_data_1.csv',
             r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\flipkart_mobile_data_2.csv', r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\flipkart_mobile_data_3.csv',
             r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\flipkart_mobile_data_4.csv', r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\flipkart_mobile_data_5.csv',
             r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data\flipkart_mobile_data_6.csv']  # Replace with your file names


# Initialize an empty list to hold DataFrames
dataframes = []

# Loop through the file list and read each file into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)  # Read each CSV file
    dataframes.append(df)   # Append DataFrame to the list

# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_file.csv', index=False)

print("All CSV files have been combined into 'combined_file.csv'.")

print("head of data", combined_df.head())
print("data shape", combined_df.shape)

folder = r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\raw_data'

combined_df.to_csv(os.path.join(folder, 'combined_df.csv'), index=False)
