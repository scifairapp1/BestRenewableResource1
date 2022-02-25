import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
# load scifair dataset
from sklearn.model_selection import train_test_split

Best_Renewable_Resource = {
    'low_temp_(f)': [35, 28, 39, 44, 50, 45, 56, 38, 37, 50, 40, 66, 63, 44, 60, 35, 36, 42, 39, 35, 43, 60, 36, 42, 48,
                     44, 52, 44, 32],
    'high_temp_(f)': [53, 56, 58, 59, 67, 58, 75, 55, 56, 64, 60, 36, 80, 64, 78, 60, 50, 64, 60, 57, 66, 78, 59, 62,
                      71, 64, 76, 62, 54],
    'precipitation_(in)': [44.85, 24.93, 39.35, 43.56, 39.74, 34.1, 49.76, 9.3, 36.82, 23.64, 42.94, 9.67, 54.69, 47,
                           52.71, 12.52, 29.13, 53.4, 37.77, 13.3, 44.75, 45.28, 34.66, 2.15, 54.37, 42.64, 53, 41.5,
                           24.31],
    'wind_speed_(mph)': [9.28, 5.21, 4.84, 6.94, 7.78, 3.83, 10.75, 9.6, 5.85, 7.85, 10.43, 6.24, 9.38, 3.69, 8.95,
                         11.63, 8.75, 6.8, 10.45, 4.3, 6.83, 8.11, 11.21, 10.96, 6.58, 8.45, 4.31, 5.83, 11.82],
    'humidity_(d)': [0.11, 0, 2.25, 2.37, 2.33, 0, 11.75, 1.94, 1.42, 0.02, 3.23, 0, 19.4, 0.008, 17.37, 0, 0.45, 0,
                     2.91, 0, 5.65, 14.78, 3.57, 3.91, 8.32, 5.34, 10.09, 3.65, 1.45],
    'cloudy_(percentage)': [50.75, 39.33, 49, 47.58, 44.75, 52.83, 44.42, 47.25, 49.75, 33.75, 46.67, 34.58, 46.75,
                            55.16, 46.83, 41.25, 54.92, 43.16, 48.67, 50.33, 42.33, 40.58, 42.92, 40.91, 42.42, 43.5,
                            43.58, 46.5, 44.58],
    'snowy_(in)': [38.4, 14.91, 59, 38.5, 15, 0.24, 0.1, 4.58, 81, 0, 37, 1.73, 0, 3, 0, 75, 119, 0.62, 16.4, 1.69, 14,
                   0, 23, 0.99, 2, 1, 0.1, 2.04, 33],
    'best_renewable_resource': [1, 2, 1, 3, 2, 1, 2, 1, 2, 2, 1, 2, 3, 1, 3, 2, 4, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1],
}

df = pd.DataFrame(Best_Renewable_Resource,
                  columns=['low_temp_(f)', 'high_temp_(f)', 'precipitation_(in)', 'wind_speed_(mph)', 'humidity_(d)',
                           'cloudy_(percentage)', 'snowy_(in)', 'best_renewable_resource'])

X = df[['high_temp_(f)', 'low_temp_(f)', 'precipitation_(in)', 'wind_speed_(mph)', 'humidity_(d)',
        'cloudy_(percentage)', 'snowy_(in)']].astype(
    float)
Y = df['best_renewable_resource'].astype(float)

# create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(df, Y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# fit a model
lm = linear_model.LinearRegression()
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

# The line / model
plt.scatter(y_test, predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')

print('Score:'), model.score(X_test, y_test)

from sklearn.model_selection import LeaveOneOut

X = np.array([[1, 2], [3, 4]])
y = np.array([1, 2])
loo = LeaveOneOut()
loo.get_n_splits(X)
for train_index, test_index in loo.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    print(X_train, X_test, y_train, y_test)
