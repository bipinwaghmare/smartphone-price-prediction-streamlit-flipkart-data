import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import os

df = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data\df.csv")

x = df.drop(['Price', 'Product_name'], axis = 1)
y = df['Price']

cat_col = x.select_dtypes(include='object')


# Dictionary to store encoders for each column
encoders = {}

# Apply LabelEncoder to each categorical column
for column in cat_col.columns:
    le = LabelEncoder()
    cat_col[column] = le.fit_transform(cat_col[column])
    encoders[column] = le  # Store the encoder for this column

# Save each encoder to a file
for column, encoder in encoders.items():
    joblib.dump(encoder, f'{column}_label_encoder.pkl')

x.update(cat_col)

columns_to_convert = ['Camera Details', 'is_5G', 'Storage_expandable', 'Display_type', 'Processor_brand', 'product_brand']

x[columns_to_convert] = x[columns_to_convert].apply(pd.to_numeric)


# sc = StandardScaler()

# x_cols = x.columns

# x = sc.fit_transform(x)

# x = pd.DataFrame(x, columns = x_cols)

folder = r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data'

# Save x and y as CSV files
x.to_csv(os.path.join(folder, 'x.csv'), index=False)
y.to_csv(os.path.join(folder, 'y.csv'), index=False)

print("Data x & y saved successfully to the specified folders!")






