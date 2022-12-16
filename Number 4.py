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

#Viewing the changes made to the dataset
Base


# In[10]:

#Number of unique overtime pay
Base.OvertimePay.nunique()


# In[11]:

#Statiscal description of dataset
Base.describe()


# In[12]:

#Maximum values of all columns in dataset
Base.max()


# In[13]:

#Minimum values of all the columns in dataset
Base.min()


# In[14]:

#Number of values of the grouped totalpay benefits of the General Manager Metropolitan Transit Authority
Base[Base.JobTitle == 'GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY'].TotalPayBenefits.shape[0]


# In[15]:

#Grouping totalpay benefits of the General Manager Metropolitan Transit Authority
Base[Base.JobTitle == 'GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY'].TotalPayBenefits


# In[16]:

#Counting the values of the grouped by year of Captain III (Police Department)
Base[Base.JobTitle == 'CAPTAIN III (POLICE DEPARTMENT)'].Year.value_counts()


# In[17]:

#Counting values of the grouped by totalpay benefits by year = 2014
Base[Base.Year == 2014].TotalPayBenefits.value_counts()


# In[18]:

#Alternative to previous
Base[Base.Year == 2014].groupby('TotalPayBenefits').count()


# In[19]:

#Top 10 highest totalpay
Base.nlargest(10, ['TotalPay'])


# In[20]:


#Alternative to previous
Base.sort_values('TotalPay', ascending = False).head(10)


# In[21]:

#Least 10 totalpay
Base.nsmallest(10, ['TotalPay'])


# In[22]:

#Alternative to previous
Base.sort_values('TotalPay').head(10)


# In[23]:

#All jobtitles that contain chief
Base[Base.JobTitle.str.contains('Chief')]


# In[24]:

#All year = 2011
Base[Base.Year == 2011]


# In[25]:

#Number of values of year = 2013
Base[Base.Year == 2013].shape[0]


# In[26]:

#All jobtitles that contain captain
Base[Base.JobTitle.str.contains('Captain')]


# In[27]:

#All employeenames = Michael
Base[Base.EmployeeName.str.contains('Micheal')]


# In[28]:

#All years in 2011, 2012
Base[Base.Year.isin(['2011', '2012'])]


# In[29]:


#Grouping JobTitle by TotalPay benefits and getting the statistical description 
Base.groupby('JobTitle').TotalPay.describe()


# In[30]:

#Grouping employeename by totalpay benefits and description
Base.groupby('EmployeeName').TotalPayBenefits.describe()


# In[31]:

#Grouping year by totalpay benefits and description
Base.groupby('Year').TotalPayBenefits.describe()


# In[32]:

#Grouping year by overtimepay and description
Base.groupby('Year').OvertimePay.describe()


# In[33]:

#Counting all the values of the years
Base.Year.value_counts()


# In[34]:

#Counting all the number of values of grouped overtimepay of 2014
Base[Base.Year == 2014].OvertimePay.value_counts().shape[0]


# In[35]:

#Alternative to previous
Base[Base.Year == 2014].OvertimePay.shape[0]


# In[36]:

#All wire robe cable maintenance mechanic in 2011
Base.loc[(Base['Year'] == 2011) & (Base['JobTitle'] == 'WIRE ROPE CABLE MAINTENANCE MECHANIC')]


# In[37]:

#Alternative to previous
Base[(Base.Year == 2011) & (Base.JobTitle == 'WIRE ROPE CABLE MAINTENANCE MECHANIC')]


# In[38]:

#Number of values of all wire robe cable maintenance mechanic in 2011 whose totalpay > 120000
Base.loc[(Base['Year'] == 2011) & (Base['JobTitle'] == 'WIRE ROPE CABLE MAINTENANCE MECHANIC') & (Base['TotalPay'] >= 120000)].shape[0]


# In[39]:

#Alternative to previous
Base[(Base.Year == 2011) & (Base.JobTitle == 'WIRE ROPE CABLE MAINTENANCE MECHANIC') & (Base.TotalPay >= 120000)].shape[0]


# In[40]:

#Using lambda function to multiply otherpay by 2
Base['OtherPay']= Base.OtherPay.apply(lambda x: x*2)
Base


# In[41]:

#Creating a new column and using lambda function as true or false
Base.insert(6,'New', Base.TotalPay.apply(lambda x: 'True' if x > 100000 else 'False'))
Base


# In[42]:

#Count plot of new column
plt.figure(figsize=(12,6))
sns.countplot(Base['New'])  


# In[43]:

#Box plot of new against year
plt.figure(figsize=(12,6))
sns.boxplot(data = Base, x = 'New', y = 'Year')


# In[44]:

#Density plot of totalpay
plt.figure(figsize=(12,6))
sns.displot(Base.TotalPay, kind = 'kde')


# In[45]:

#Correlation of the dataset
plt.figure(figsize = (10,5))
sns.heatmap(Base.corr(), annot = True, fmt = '0.1f')


# In[46]:

#Pie chart of year
Base.Year.value_counts().plot(kind = 'pie', figsize = (6,6))


# In[47]:

#Bar chart of new column
Base.New.value_counts().plot(kind = 'bar', figsize = (6,6))


# In[ ]:




