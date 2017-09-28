# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:59:06 2017

@author: sarwesh suman
"""

import pandas as pd
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix

file_name = r'C:\Users\bgh47373\Documents\Module -2\part1\classification\diabetes.csv'

df_diabities = pd.read_csv(file_name)

print(df_diabities.shape)

""" 
This is sample data of diabitic patients, the goal it to predict if the patient is diabitic or not 
If the patient is diabetic then the outcome will be 1, there are two classes only, 0 or 1
"""

# Pre processing steps

# shuffling because we dont want data in serial order
df_diabities = shuffle(df_diabities)

X=df_diabities.ix[:,:-1] # Last column is Outcome or class to predict
Y=df_diabities.ix[:,-1] # Outcome with value 0 or 1

# Lets create train test data

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

# Building the model

# Within Naive Bayes we have three options
# 1. BernoulliNB 
#   Best when predictions are to be made from binary features
# 2. GaussianNB
#   Best for making predictions from normally distributed data
# 3. MultinomialNB
#   Best for making discrete class predictions

model = GaussianNB()
model.fit(X_train,Y_train)

# prediction

Y_pred = model.predict(X_test)

# evaluation model

print(accuracy_score(Y_test,Y_pred))
print(classification_report(Y_test,Y_pred))
cmatrix = confusion_matrix(Y_test,Y_pred)
print(cmatrix)

tp , fp, fn , tn = cmatrix.ravel()

print("Sensitivity = ",tp/(tp+fn))
print("Specificity =", tn/(tn+fp))
print("Accuracy=",(tp+fn)/(tp+fn+fp+fn))