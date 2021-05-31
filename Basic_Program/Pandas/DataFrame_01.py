#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Install a pip package in the current Jupyter kernel
import sys
get_ipython().system('{sys.executable} -m pip install pandas')


# In[3]:


import pandas as pd
df = pd.read_csv("D:\Python\Pandas\weather.csv")


# In[5]:


df


# In[6]:


df.Temperature.max()


# In[7]:


df['Temperature'].max()


# In[8]:


df['EST'][df['Events'] == 'Rain']


# In[14]:


df.fillna(0, inplace=True)
df['WindSpeedMPH'].mean()


# In[15]:


df['WindSpeedMPH'].mode()


# In[16]:


df['WindSpeedMPH'].median()


# In[17]:


df['TestData1'] + df['TestDataB']


# In[18]:


df.describe()


# In[22]:


weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
df = pd.read_csv("weather_data.csv")
df


# In[24]:


df.shape


# In[25]:


rows, columns = df.shape


# In[26]:


rows


# In[27]:


columns


# In[28]:


df.head()


# In[29]:


df.head(2)


# In[30]:


df.tail()


# In[31]:


df.tail(1)


# In[33]:


df[2:5]


# In[34]:


df.columns


# In[35]:


df.day


# In[37]:


df.event
df['event']


# In[38]:


type(df['event'])


# In[40]:


df[['event', 'day', 'temperature']]


# In[41]:


df


# In[43]:


df.temperature.max()


# In[44]:


df.temperature.mean()


# In[45]:


df.temperature.std()


# In[46]:


df.describe()


# In[47]:


df[df.temperature >= 32]


# In[49]:


df[df.temperature == df.temperature.max()]


# In[54]:


df['day'][df.temperature == df.temperature.max()]


# In[56]:


df[['day','temperature']][df.temperature == df.temperature.max()]


# In[57]:


df


# In[58]:


df.index


# In[ ]:


df.set_index('day', inplace=True)


# In[69]:


df


# In[71]:


df.loc['1/1/2017']


# In[72]:


df.reset_index(inplace=True)


# In[73]:


df


# In[74]:


df.set_index('event', inplace=True)


# In[75]:


df


# In[77]:


df.loc['Snow']

