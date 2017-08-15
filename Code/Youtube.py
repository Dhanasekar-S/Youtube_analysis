import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor

## Loading csv input data
def load_data():
    return pd.read_csv('data.csv')

##Normalizing data and splitting into train and test
##Input and output features are assigned here too
def split_data(df):
    scaler = MinMaxScaler()
    scaler.fit(df)
    MinMaxScaler(copy=True, feature_range=(0, 1))
    scaler.transform(df)
    df.dropna()
    train, test = train_test_split(df, test_size=0.10,random_state=100)
    train_x = train[['commentCount','dislikeCount','viewCount','views/subscribers']]
    train_y = train['likeCount']
    test_x = test[['commentCount','dislikeCount','viewCount','views/subscribers']]
    test_y = test['likeCount']
    return train_x, train_y, test_x, test_y

##Calling the above functions
df = load_data()
tr_x, tr_y, ts_x, ts_y = split_data(df)

#Previewing the data
print(tr_x.head())

##Training a Random Forest Regressor with 500 Trees
clf = RandomForestRegressor(n_estimators=500, max_features='auto', verbose=50, n_jobs=-1)
print('Training Started')

#Fitting the training data
clf.fit(tr_x, tr_y)
print('Training Finished')

#Training Accuracy
print("Training Score")
print(clf.score(tr_x, tr_y))

#Test Accuracy
print("Test Score")
print(clf.score(ts_x, ts_y))

# Predict the number of likes of any youtube video by providing the four features- comment, dislike, views and video popularity
print(clf.predict([[6866, 9735, 5525110, 1.668293]]))