import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

wthr_condns = pd.read_csv(r'weather.csv')
df = DataFrame(wthr_condns,columns=['Week','MinTemp','MaxTemp','Rainfall','Evaporation','Humidity','Pressure','Blight'])

X = df[['MinTemp','MaxTemp','Rainfall','Evaporation']]
Y = df['Blight']
 
# with Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# prediction with sklearn
lweek_MinTemp = 12.4
lweek_MaxTemp = 32.0
lweek_Rainfall = 2.4
lweek_Evaporation = 8.2
print ('Predicted Blight probability with sklearn: ', regr.predict([[lweek_MinTemp,lweek_MaxTemp,lweek_Rainfall,lweek_Evaporation]]))
print ('Predicted Blight probability with linear regression:',regr.intercept_ + (regr.coef_[0]*lweek_MinTemp) + (regr.coef_[1]*lweek_MaxTemp)+ (regr.coef_[2]*lweek_Rainfall)+(regr.coef_[3]*lweek_Evaporation))



