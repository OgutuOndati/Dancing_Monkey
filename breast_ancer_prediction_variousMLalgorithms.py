# -*- coding: utf-8 -*-
"""Breast_ancer_prediction_VariousMLalgorithms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QMj2CP8j9ggNfIDrugBS1cMZ-AET_nAE
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



dataset = pd.read_csv('data.csv')
dataset

dataset.isna().any()
dataset[dataset.columns[dataset.isnull().any()]]
#dataset['Unnamed: 32'] = dataset['Unnamed: 32'].fillna(dataset['Unnamed: 32'].mean())

print(dataset.shape)
print(dataset.head(5))

""" MAPPING STRING VALUES TO NUMBERS"""

dataset['diagnosis'] = dataset['diagnosis'].map({'B':0, 'M':1}).astype(int)
print(dataset.head)

"""segregate dataset to x and y"""

X = dataset.iloc[:,2:232].values
X

Y = dataset.iloc[:,1].values
Y

"""split into train and test"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25,random_state=0)

"""Feature Scaling
we scale our data to make sure all features contribute equally to the result 
Fit_Transform_Fit method is calculating the mean and the variance of each of the features present in our data
Transform method is transforming all the features using the respective mean and variance.
We want our data to be a completely new and surprising set for our model

"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)
print(X_test)

"""VALIDATING SOME ML ALGOS BY ITS ACCURACY-MODEL SCORE"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.tree  import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

models=[]
models.append(('LR', LogisticRegression(solver= 'liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
print(models)

results= []
names = []
res = []
for name, model in models:
  kfold = StratifiedKFold(n_splits=10, random_state=None)
  cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
  results.append(cv_results)
  names.append(name)
  res.append(cv_results.mean())
  print('%s:%f' %(name, cv_results.mean()))

plt.ylim(.900, .999)
plt.bar(names, res, color = 'purple', width = 0.6)

plt.title('Algorithm Comparison')
plt.show()

"""Training and prediction using algorithm with high accuracy...as seen above its linear regression"""

model = LogisticRegression(solver= 'liblinear', multi_class='ovr')
model.fit(X_train, y_train)
value =[[13.71,	20.83,	90.2,	577.9,	0.1189,	0.1645,	0.09366, 0.05985, 0.2196,0.07451,0.5835,1.377,3.856,50.96,0.008805,0.03029,0.02488,0.01448,0.01486,0.005412,17.06,28.14,110.6,897,0.1654,0.3682,0.2678,0.1556,	0.3196,	0.1151]]
y_pred = model.predict(value)
print(y_pred)
