#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[5]:


df=pd.read_csv(r"HR-Employee-Attrition.csv")
pd.set_option('display.max_columns', None)
df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.describe(include="O")


# In[9]:


sns.countplot(x=df.Attrition)
plt.show()


# In[10]:


sns.countplot(hue=df.Attrition, x=df.BusinessTravel)
plt.show()


# In[11]:


sns.countplot(hue=df.Attrition, x=df.Department)
plt.show()


# In[12]:


sns.countplot(x=df.Attrition, hue=df.EducationField)
plt.show()


# In[13]:


sns.countplot(x=df.Attrition, hue=df.Gender)
plt.show()


# In[14]:


sns.countplot(hue=df.Attrition , x=df.OverTime)
plt.show()


# In[15]:


plt.figure(figsize=(20,10), facecolor='white')
sns.countplot(x='JobRole' , hue='Attrition', data=df)
plt.xlabel('JobRole' ,fontsize=10)


# In[16]:


numerical_col = []
for column in df.columns:
    if df[column].dtype == "int64" and len(df[column].unique())>= 10:
        
        numerical_col.append(column)


# In[17]:


numerical_col


# In[19]:


data = df[['Age',
 'DailyRate',
 'DistanceFromHome',
 'EmployeeNumber',
 'HourlyRate',
 'MonthlyIncome',
 'MonthlyRate',
 'NumCompaniesWorked',
 'PercentSalaryHike',
 'TotalWorkingYears',
 'YearsAtCompany',
 'YearsInCurrentRole',
 'YearsSinceLastPromotion',
 'YearsWithCurrManager']]


# In[20]:


plt.figure(figsize=(20,25), facecolor='white')
plotnumber = 1

for column in data:
    if plotnumber <= 16:
        ax =plt.subplot(4,4,plotnumber)
        sns.histplot(x=data[column].dropna(axis=0)
                    , hue= df.Attrition)
        plt.xlabel(column, fontsize=20)
        plt.ylabel('Attrition', fontsize=20)
    plotnumber+=1
plt.tight_layout()


# In[21]:


sns.histplot(hue=df.Attrition,x=df.Age)
plt.show()


# In[22]:


sns.histplot(hue=df.Attrition,x=df.DistanceFromHome)
plt.show()


# In[23]:


sns.histplot(x= df.MonthlyIncome, hue=df.Attrition)
plt.show()


# In[24]:


sns.histplot(hue=df.Attrition, x=df.NumCompaniesWorked)
plt.show()


# In[25]:


from sklearn.ensemble import RandomForestClassifier


# In[26]:


rfc = RandomForestClassifier(n_estimators=100)


# In[ ]:




