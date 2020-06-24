# importing libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import pickle

# creating dataframe
train_data=pd.read_csv('C:/Users/Nishtha/Downloads/train.csv')

# assigning independent (X_train) and dependent (Y_train) variables
X_train=train_data[["Pclass","SibSp","Parch","Sex","Fare"]]
Y_train=train_data['Survived']

#Fitting the model with training set
rr=Ridge(alpha=0.01)
rr.fit(X_train,Y_train)

# intercepts and coefficients of the fitted model
intercept=rr.intercept_
coefficients=rr.coef_

# saving model
pickle.dump(rr,open('./Flaskapp/Ridge_Titanic.pkl','wb'))

# alternative code to store the coefficients that can be further load and used to make predictions
'''
print(intercept, file=open("Outputs.txt", "a"))
for i in range(len(coefficients)):
    print(coefficients[i],file=open("Outputs.txt","a"))
    i=i+1
'''
