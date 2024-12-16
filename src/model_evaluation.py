from sklearn import metrics
import pandas as pd
import numpy as np
import pickle
import os
import joblib
from sklearn.ensemble import GradientBoostingRegressor

x_train = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data\x_train.csv")
x_test = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data\x_test.csv")
y_train = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data\y_train.csv")
y_test = pd.read_csv(r"C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\data\clean_data\y_test.csv")

model_path = r'C:\Users\Bipin\Downloads\DL Practice\Deployment of flipkart scrapped data project\model.pkl'

gbr = pickle.load(open(model_path, 'rb'))

y_pred = gbr.predict(x_test)

prediction = gbr.predict(x_test)

gbr.score(x_test,y_test)

gbr.score(x_train,y_train)

print('MAE:',metrics.mean_absolute_error(y_test,prediction))
print('MSE:',metrics.mean_squared_error(y_test,prediction))
print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,prediction)))







