#!/usr/bin/env python
# coding: utf-8

# # importing the dependencies

# In[1]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[2]:


url="https://www.dropbox.com/scl/fi/0uiujtei423te1q4kvrny/diabetes.csv?rlkey=20xvytca6xbio4vsowi2hdj8e&st=uv8fbcue&dl=1"
diabetes_dataset=pd.read_csv(url)


# In[3]:


diabetes_dataset.head()


# In[4]:


diabetes_dataset.shape # number of rows and column


# In[5]:


diabetes_dataset.describe() # statistical measure of data


# In[6]:


diabetes_dataset['Outcome'].value_counts()


# In[7]:


diabetes_dataset.groupby('Outcome').mean()


# In[8]:


# separating the data and labels


# In[9]:


X = diabetes_dataset.drop(columns='Outcome',axis=1)
Y= diabetes_dataset['Outcome']


# In[10]:


print(X)


# #Data Standardization

# In[11]:


scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)


# In[12]:


print(standardized_data)


# In[13]:


X= standardized_data
Y= diabetes_dataset['Outcome']


# In[14]:


print(X)
print(Y)


# In[15]:


#Train Test Split


# In[16]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2,stratify=Y,random_state=2)


# In[17]:


print(X.shape ,X_train.shape,X_test.shape)


# #Training the Model

# In[18]:


classifier = svm.SVC(kernel = 'linear')


# In[19]:


#training the support vector Machine Classifier


# In[20]:


classifier.fit(X_train, Y_train)


# #Model Evaluation

# #Accuracy Score

# In[21]:


#accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)


# In[22]:


print('Accuracy score of the training data : ',training_data_accuracy)


# In[23]:


#accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)


# In[24]:


print('Accuracy score of the test data : ',test_data_accuracy)


# #Making a Predictive System

# In[25]:


input_data = (4,110,92,0,0,37.6,0.191,30)

#changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)
# reshape the array
input_data_reshaped =input_data_as_numpy_array.reshape(1,-1)  

# standardize the input data

std_data=scaler.transform(input_data_reshaped)
prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0]==0):
    print('The person is not diabetic')
else:
    print('The Person is diabetic')


# In[ ]:





# #Saving the trained model

# In[26]:


import pickle


# In[27]:


filename = 'trained_model.sav'
pickle.dump(classifier , open(filename,'wb'))


# In[28]:


#loading the saved model
loaded_model = pickle.load(open('trained_model.sav' , 'rb'))


# In[29]:


input_data = (4,110,92,0,0,37.6,0.191,30)

#changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)
# reshape the array
input_data_reshaped =input_data_as_numpy_array.reshape(1,-1)  

# standardize the input data

std_data=scaler.transform(input_data_reshaped)
prediction = loaded_model.predict(std_data)
print(prediction)

if (prediction[0]==0):
    print('The person is not diabetic')
else:
    print('The Person is diabetic')


# In[ ]:




