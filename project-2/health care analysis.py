#!/usr/bin/env python
# coding: utf-8

# In[11]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


df = pd.read_csv('KaggleV2-May-2016.csv')


# In[18]:


df.head()


# In[19]:


df.shape


# In[20]:


df.duplicated().sum()


# In[21]:


df['PatientId'].duplicated().sum()


# In[22]:


df['PatientId'].nunique()


# In[23]:


a = 62299
s = 48228
a+s


# In[24]:


df.duplicated(['PatientId' , 'No-show']).sum()


# In[26]:


df.info()


# In[27]:


df.describe()


# In[28]:


df[df["Age"] == -1]


# In[29]:


df.drop(index =99832 ,inplace = True )


# In[30]:


df.describe()


# In[31]:


df.rename(columns = {"Hipertension" : "Hypertension"} , inplace= True)

df.rename(columns = {"No-show" : "No_show"} , inplace= True)


# In[32]:


df.head()


# In[33]:


df.drop_duplicates(["PatientId", "No_show"], inplace= True)


# In[34]:


df.shape


# In[35]:


df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'],axis = 1 ,inplace = True)


# In[36]:


df.head()


# In[37]:


df.shape


# In[38]:


df.hist(figsize=(16,7));


# In[39]:


show = df.No_show == "No"
Nshow = df.No_show == "Yes"


# In[40]:


df[show].count(), df[Nshow].count()


# In[41]:


def attend (df, age , showw, nshow):
    plt.figure(figsize=[16,5])
    df[age][show].hist(alpha = .5 , bins = 10, color ='r')
    df[age][Nshow].hist(alpha = .5 , bins = 10, color ='g')
    plt.legend();
    plt.title("comperision age & patient_show")
    plt.xlabel("Age")
    plt.ylabel("PatientNum")
    plt.show()
    
attend(df, "Age" ,show , Nshow)  


# In[42]:


df


# In[43]:


print(df.dtypes)


# In[44]:


# Assuming show and Nshow are defined correctly
plt.figure(figsize=[12, 5])

# Plotting mean age for patients who showed up
df[show].groupby(['Hypertension', 'Diabetes'])['Age'].mean().plot(kind='bar', color='r', alpha=0.7, label='Show')

# Plotting mean age for patients who did not show up
df[Nshow].groupby(['Hypertension', 'Diabetes'])['Age'].mean().plot(kind='bar', color='b', alpha=0.7, label='No Show')

plt.legend()
plt.title("Comparison of Hypertension and Diabetes to Mean Age of Patients")
plt.xlabel("Hypertension, Diabetes Status")
plt.ylabel("Mean Age")
plt.xticks(rotation=0)
plt.show()


# In[45]:


df[show].groupby(['Hypertension', 'Diabetes'])['Age'].mean(),df[Nshow].groupby(['Hypertension', 'Diabetes'])['Age'].mean()


# In[48]:


plt.figure(figsize=[12, 5])

# Plotting mean age for patients who showed up
df[show].groupby("Gender")['Age'].mean().plot(kind='bar', color='b', alpha=0.7, label='Show')

# Plotting mean age for patients who showed up
df[Nshow].groupby("Gender")['Age'].mean().plot(kind='bar', color='r', alpha=0.7,label='Nshow')
plt.legend();
plt.title("comperision gender & patient_show") 
plt.xlabel("Gender")
plt.ylabel("mean age")
plt.xticks(rotation=0)
plt.show()


# In[ ]:




