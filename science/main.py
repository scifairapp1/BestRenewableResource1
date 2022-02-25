import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.preprocessing import LabelEncoder as le

df = pd.read_csv('scifair.csv')

'''.apply(preprocessing.LabelEncoder().fit_transform)'''
x = df.drop('best renewable source', axis=1)
y = df['best renewable source']
print(x.shape)
print(y.shape)
# importing train_test_split from sklearn

# splitting the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# creating an object of LinearRegression class
LR = LinearRegression()
# fitting the training data
LR.fit(x_train, y_train)
y_prediction = LR.predict(x_test)
print(y_prediction)
score = r2_score(y_test, y_prediction)
print('r2 socre is ', score)
print('mean_sqrd_error is==', mean_squared_error(y_test, y_prediction))
print('root_mean_squared error of is==', np.sqrt(mean_squared_error(y_test, y_prediction)))
