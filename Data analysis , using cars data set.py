#!/usr/bin/env python
# coding: utf-8

# In[1]:


#cars dataset


# In[2]:


import pandas as pd


# In[3]:


car=pd.read_csv("/home/erick/Downloads/CarPrice_Assignment.csv")


# In[4]:


car


# In[5]:


car.head()


# In[6]:


car.shape


# In[7]:


car.isnull


# In[11]:


car['horsepower'].fillna(car['citympg'].mean(),inplace=True)


# In[12]:


car


# In[16]:


car['citympg'].mean()


# In[17]:


car.head(2)


# In[20]:


car['stroke'].value_counts()


# In[21]:


#removing unwanted records 


# In[22]:


car.head()


# In[24]:


car[car['price']<10000]


# In[25]:


#removing all the cars with price less than 10,000


# In[28]:


car[~(car['price']<10000)]


# In[29]:


#increasing all the horsepower by 3


# In[30]:


car.head()


# In[31]:


car['horsepower']=car['horsepower'].apply(lambda x:x+3)


# In[32]:


car


# In[ ]:




