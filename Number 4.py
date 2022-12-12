#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Read Csv File
Base = pd.read_csv('Salaries.csv')


# In[3]:


Base


# In[4]:


#First five rows of Csv File
Base.head()


# In[5]:


#Last Five rows of Csv file
Base.tail()


# In[6]:


#Checking for null values
Base.isnull().sum()


# In[7]:


#Data cleaning by dropping all null value columns
Base.dropna(axis = 1, inplace = True)


# In[8]:

#Number of unique values
Base.Year.nunique()


# In[9]:


Base


# In[10]:


Base.OvertimePay.nunique()


# In[11]:


Base.describe()


# In[12]:


Base.max()


# In[13]:


Base.min()


# In[14]:


Base[Base.JobTitle == 'GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY'].TotalPayBenefits.shape[0]


# In[15]:


Base[Base.JobTitle == 'GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY'].TotalPayBenefits


# In[16]:


Base[Base.JobTitle == 'CAPTAIN III (POLICE DEPARTMENT)'].Year.value_counts()


# In[17]:


Base[Base.Year == 2014].TotalPayBenefits.value_counts()


# In[18]:


Base[Base.Year == 2014].groupby('TotalPayBenefits').count()


# In[19]:


Base.nlargest(10, ['TotalPay'])


# In[20]:


#Alternative to previous
Base.sort_values('TotalPay', ascending = False).head(10)


# In[21]:


Base.nsmallest(10, ['TotalPay'])


# In[22]:


Base.sort_values('TotalPay').head(10)


# In[23]:


Base[Base.JobTitle.str.contains('Chief')]


# In[24]:


Base[Base.Year == 2011]


# In[25]:


Base[Base.Year == 2013].shape[0]


# In[26]:


Base[Base.JobTitle.str.contains('Captain')]


# In[27]:


Base[Base.EmployeeName.str.contains('Micheal')]


# In[28]:


Base[Base.Year.isin(['2011', '2012'])]


# In[29]:


#Grouping JobTitle by TotalPay and getting the statistical description of TotalPay
Base.groupby('JobTitle').TotalPay.describe()


# In[30]:


Base.groupby('EmployeeName').TotalPayBenefits.describe()


# In[31]:


Base.groupby('Year').TotalPayBenefits.describe()


# In[32]:


Base.groupby('Year').OvertimePay.describe()


# In[33]:


Base.Year.value_counts()


# In[34]:


Base[Base.Year == 2014].OvertimePay.value_counts().shape[0]


# In[35]:


Base[Base.Year == 2014].OvertimePay.shape[0]


# In[36]:


Base.loc[(Base['Year'] == 2011) & (Base['JobTitle'] == 'WIRE ROPE CABLE MAINTENANCE MECHANIC')]


# In[37]:


Base[(Base.Year == 2011) & (Base.JobTitle == 'WIRE ROPE CABLE MAINTENANCE MECHANIC')]


# In[38]:


Base.loc[(Base['Year'] == 2011) & (Base['JobTitle'] == 'WIRE ROPE CABLE MAINTENANCE MECHANIC') & (Base['TotalPay'] >= 120000)].shape[0]


# In[39]:


Base[(Base.Year == 2011) & (Base.JobTitle == 'WIRE ROPE CABLE MAINTENANCE MECHANIC') & (Base.TotalPay >= 120000)].shape[0]


# In[40]:


Base['OtherPay']= Base.OtherPay.apply(lambda x: x*2)
Base


# In[41]:


Base.insert(6,'New', Base.TotalPay.apply(lambda x: 'True' if x > 100000 else 'False'))
Base


# In[42]:


plt.figure(figsize=(12,6))
sns.countplot(Base['New'])  


# In[43]:


plt.figure(figsize=(12,6))
sns.boxplot(data = Base, x = 'New', y = 'Year')


# In[44]:


plt.figure(figsize=(12,6))
sns.displot(Base.TotalPay, kind = 'kde')


# In[45]:


plt.figure(figsize = (10,5))
sns.heatmap(Base.corr(), annot = True, fmt = '0.1f')


# In[46]:


Base.Year.value_counts().plot(kind = 'pie', figsize = (6,6))


# In[47]:


Base.New.value_counts().plot(kind = 'bar', figsize = (6,6))


# In[ ]:




