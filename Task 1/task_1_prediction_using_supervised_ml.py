# -*- coding: utf-8 -*-
"""Task 1 Prediction using Supervised ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XSsQJrmkriud_Esg5_nvFMTeUoYHMsDh
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline

#Reading csv from github
csv = "https://raw.githubusercontent.com/Darsh06/Spark-Foundation/master/Task%201/Task%201.csv"
data = pd.read_csv(csv)

data.head(10)

#Plotting Graph of the given data
data.plot(x="Hours", y="Scores", style='1', color='red')
plt.title("Hours v/s Percentage")
plt.xlabel("No of Hours Studied")
plt.ylabel("Percentage Scored")
plt.show()

#Splitting Columns 
X = data.iloc[:,:-1].values
Y = data.iloc[:,1].values

#SPLITTING DATA into 70 - 30 
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

#Fitting the linear regression model
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# Plotting the regression line
line = regressor.coef_*X+regressor.intercept_

# Plotting for the test data
data.plot(x="Hours", y="Scores", style='1', color='red')
# plt.scatter(X, Y,color='red')
plt.plot(X, line,color='red',linewidth=0.1);
plt.show()

print(X_test) # Testing data - In Hours
y_pred = regressor.predict(X_test) # Predicting the scores

# Comparing Actual vs Predicted
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df

hour = [[9.25]]
own_pred = regressor.predict(hour)
print("No of Hours = {}".format(hour))
print("Predicted Score = {}".format(own_pred[0]))

hour = [[6.54]]
own_pred = regressor.predict(hour)
print("No of Hours = {}".format(hour))
print("Predicted Score = {}".format(own_pred[0]))

hour = [[4.13]]
own_pred = regressor.predict(hour)
print("No of Hours = {}".format(hour))
print("Predicted Score = {}".format(own_pred[0]))

#Evaluating Mean Absolute Error
from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred))