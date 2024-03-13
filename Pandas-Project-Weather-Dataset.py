#!/usr/bin/env python
# coding: utf-8

# # Upload the dataset

# In[4]:


pip install pandas


# In[5]:


import pandas as pd


# In[6]:


df = pd.read_csv(r"C:\Users\A.S.Pride\Downloads\file.csv")


# # Reading CSV file

# In[7]:


df.head()


# In[8]:


df.shape


# In[9]:


df.index


# In[10]:


df.columns


# In[18]:


df.dtypes


# In[11]:


df["Weather"].unique()


# In[22]:


df["Weather"].nunique()


# In[23]:


df.count()


# In[24]:


df["Weather"].value_counts()


# In[25]:


df.info()


# # Q1: Find all the unique "wind speed" values in the data

# In[26]:


df.head(2)


# In[27]:


df["Wind Speed_km/h"].unique()


# In[29]:


df["Wind Speed_km/h"].nunique()


# # Q2: Find the number of times when the weather is exactly clear

# In[31]:


df.Weather.value_counts()


# In[33]:


df[df.Weather == "Clear"]


# # Find the number of times when the wind speed was exactly 4 knh

# In[34]:


df.head(2)


# In[37]:


df[df["Wind Speed_km/h"] == 4]


# In[38]:


df["Wind Speed_km/h"].value_counts()


# # Find out the null values in the data

# In[39]:


df.isnull().sum()


# In[41]:


df.notnull().sum()


# # Q5: Rename the column name "Weather" of the data frame to "Weather Condition"

# In[44]:


df.rename(columns = {"Weather": "Weather Condition"}, inplace = True)


# In[45]:


df.head(2)


# # Q6: What is the mean of visibilty?

# In[12]:


df.Visibility_km.mean()


# #  Q7: What is the standard deviation of Pressure in the data?

# In[13]:


df.Press_kPa.std()


# # Q8: What is the variance of relative humidity in the data?

# In[14]:


df["Rel Hum_%"].var()


# # Q9: Find all intances where snow was recorded?

# In[15]:


df.head(2)


# In[16]:


df.Weather.value_counts()


# In[18]:


df[df.Weather == "Snow"]


# In[20]:


df[df.Weather.str.contains("Snow")]


# # Q11: What is the mean value of each column against each Weath Condition?

# In[21]:


df.groupby("Weather").mean()


# # Q12: Find all instances where weather is clear or Visibilty is above 40?

# In[22]:


df.head(2)


# In[31]:


df[(df['Weather'] == "Clear") | (df['Visibility_km'] > 40)]


# # Q13: Find all instances Weather is clear and Relative humidity is greater then 50 or Visibilty is above 40

# In[32]:


df.head(2)


# In[36]:


filtered_df = df[(df["Weather"] == "Clear") & (df["Rel Hum_%"] > 50) | (df["Visibility_km"] > 40)]


# In[ ]:




