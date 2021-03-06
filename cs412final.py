# -*- coding: utf-8 -*-
"""cs412Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uRTg04tvzZpFzYyiwqAgAMaAxdelO4ow



#Collab Link
https://colab.research.google.com/drive/1uRTg04tvzZpFzYyiwqAgAMaAxdelO4ow

# Data Loading
"""

!pip install scikit-plot

from sklearn.utils import shuffle
import pandas as pd 

from google.colab import drive
drive.mount('/content/drive')

# Read data from file 'credit_german_train.csv' using read_csv() function
trainData = pd.read_csv("/content/drive/My Drive/LoanData_Train/TrainPortion_Data.csv")
labelData = pd.read_csv("/content/drive/My Drive/LoanData_Train/TrainPortion_Label_.csv")
#open('/content/drive/My Drive/LoanData_Train/TrainPortion_Label_.csv')

#Concatenate label data with training data
unitedData = pd.concat([trainData, labelData], axis=1, join_axes=[trainData.index])

"""# Data Exploring"""

import matplotlib.pyplot as plt

#Check empty cells in data 
# -if the mean is above 0.90 we are going to drop these attributes
print(unitedData.isnull().mean())


# We found that these 3 columns are almost empty
unitedData = unitedData.drop(columns=['annual_inc_joint'])
unitedData = unitedData.drop(columns=['dti_joint'])
unitedData = unitedData.drop(columns=['desc'])

#For plotting histograms to check whether attributes is needed or unrelevant
import matplotlib.pyplot as plt

#Histogram Plot
table=pd.crosstab(unitedData.application_type,unitedData.charged_off)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of application type and credit given')
plt.xlabel('application type')
plt.ylabel('Proportion')

#Application type is not a good attribute
# -We will drop this column
unitedData = unitedData.drop(columns=['application_type'])

#We take the mod of the columns and fill it with mod.
# -We didnt loose characteristics of data.
# -Approx. 500k data is preserved. 

# emp_title /nan'ları meanle doldurma
unitedData.emp_title.fillna((unitedData.emp_title.mode()[0]), inplace=True)

#emp_length
unitedData.emp_length.fillna((unitedData.emp_length.mode()[0]), inplace=True)

#dti
unitedData.dti.fillna((unitedData.dti.mode()[0]), inplace=True)

#total_bal_il  
unitedData.total_bal_il.fillna((unitedData.total_bal_il.mode()[0]), inplace=True)

#il_util  
unitedData.il_util.fillna((unitedData.il_util.mode()[0]), inplace=True)

#max_bal_bc  
unitedData.max_bal_bc.fillna((unitedData.max_bal_bc.mode()[0]), inplace=True)

#all_util  
unitedData.all_util.fillna((unitedData.all_util.mode()[0]), inplace=True)

#inq_fi  
unitedData.inq_fi.fillna((unitedData.inq_fi.mode()[0]), inplace=True)

#total_cu_tl  
unitedData.total_cu_tl.fillna((unitedData.total_cu_tl.mode()[0]), inplace=True)

#inq_last_12m  
unitedData.inq_last_12m.fillna((unitedData.inq_last_12m.mode()[0]), inplace=True)

#Check dimensinality 
unitedData.shape

import numpy as np
#Check the column purpose classes counts 
print(unitedData['purpose'].value_counts())

## purpose ##
#Unsignificant number of data merged to 'other'
unitedData['purpose']=np.where(unitedData['purpose'] =='renewable_energy', 'other', unitedData['purpose'])
unitedData['purpose']=np.where(unitedData['purpose'] =='house', 'other', unitedData['purpose'])
unitedData['purpose']=np.where(unitedData['purpose'] =='vacation', 'other', unitedData['purpose'])
unitedData['purpose']=np.where(unitedData['purpose'] =='moving', 'other', unitedData['purpose'])
unitedData['purpose']=np.where(unitedData['purpose'] =='small_business', 'other', unitedData['purpose'])
unitedData['purpose']=np.where(unitedData['purpose'] =='car', 'other', unitedData['purpose'])
unitedData['purpose']=np.where(unitedData['purpose'] =='medical', 'other', unitedData['purpose'])
unitedData['purpose']=np.where(unitedData['purpose'] =='major_purchase', 'other', unitedData['purpose'])

#Purpose and title has similar classes, purpose have less classes than title, 
# -So, we wanted to keep purpose instead of title
# -Title, needs to be dropped 

## title ## very diverged data can not be merged as we did on purpose
unitedData = unitedData.drop(columns=['title'])

#Term and emp_length have both string and integer in it.
# -Strings are removed
# -Integer part is left in data

#Term'den stringleri sildim
unitedData.term = unitedData.term.str.extract('(\d+)')
print(unitedData.term.head())

#Emp_length'den stringleri sildim
unitedData.emp_length = unitedData.emp_length.str.extract('(\d+)')
print(unitedData.emp_length.head())

#Dummy variable oluşturma, alternatif OneHotEncoder

purpose_dummy = pd.get_dummies(unitedData.purpose)
unitedData = unitedData.join(purpose_dummy)
unitedData.pop('purpose')

home_dummy = pd.get_dummies(unitedData.home_ownership)
unitedData = unitedData.join(home_dummy)
unitedData.pop('home_ownership')

vs_dummy = pd.get_dummies(unitedData.verification_status)
unitedData = unitedData.join(vs_dummy)
unitedData.pop('verification_status')

#We found that from the histogram above this feature has no effect on classification
unitedData.pop('initial_list_status')

#other unwanted data

unitedData.pop('zip_code')
unitedData.pop('earliest_cr_line')
unitedData.pop('emp_title')
unitedData.pop('addr_state')

#in case we missed an attribute
unitedData = unitedData.dropna()

#lastly labels
labels = unitedData.pop('charged_off')

"""# Logistic Regression"""

from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split


# Shuffle the training data
ShuffledTrainData, ShuffledLabelData = shuffle(unitedData, labels, random_state=0)


X_train,X_test,y_train,y_test=train_test_split(ShuffledTrainData,ShuffledLabelData,test_size=0.25,random_state=0)
# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)

from sklearn.metrics import accuracy_score

#Test score with test training data
accuracy_score(y_test,logreg.predict(X_test))

"""# RoC"""

from __future__ import absolute_import
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits as load_data
import scikitplot as skplt



probas = logreg.predict_proba(X_test)
skplt.metrics.plot_roc(y_true=y_test, y_probas=probas)
plt.show()