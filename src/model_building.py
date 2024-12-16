import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import joblib
import pickle

x = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data\x.csv")
y = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data\y.csv")

# xtrain fit transform
# xtest transform

x_train, x_test, y_train, y_test =train_test_split(x, y, test_size=0.2, random_state=42 )

sc = StandardScaler()

x_train_cols = x_train.columns

x_train = sc.fit_transform(x_train)

x_train = pd.DataFrame(x_train, columns = x_train_cols)

x_test_cols = x_test.columns

x_test = sc.transform(x_test)

x_test = pd.DataFrame(x_test, columns = x_test_cols)
print(x_train.columns==x_test.columns)

folder = r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data'

# Save x and y as CSV files
x_train.to_csv(os.path.join(folder, 'x_train.csv'), index=False)
x_test.to_csv(os.path.join(folder, 'x_test.csv'), index=False)

y_train.to_csv(os.path.join(folder, 'y_train.csv'), index=False)
y_test.to_csv(os.path.join(folder, 'y_test.csv'), index=False)

joblib.dump(sc, r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\scaler.pkl')

from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor()

gbr.fit(x_train, y_train)

pred = gbr.predict(x_test)

# print("pred", len(pred))
# print("y_test", len(y_test))
print("Score for train", gbr.score(x_train, y_train))
print("Score for test", gbr.score(x_test, y_test))

# residual = y_test - pred

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

mae = mean_absolute_error(y_test, pred)
mape = mean_absolute_percentage_error(y_test, pred)
mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))

print("Mean absolute error :", mae)
print("Mean absolute percentage error :", mape)
print("Mean squared error :", mse)
print("Square root of Mean squared error :", rmse)

# Save the model and the scaler
model_path = r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\model.pkl'

# Save the model using pickle
with open(model_path, 'wb') as file:
    pickle.dump(gbr, file)







