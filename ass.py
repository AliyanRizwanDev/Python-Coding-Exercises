#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
import numpy as np


# In[25]:


df = pd.read_csv('jsrt_metadata.csv')


# In[26]:


df


# In[27]:


df['diagnosis'].value_counts()


# In[28]:


df.isnull().sum()


# In[40]:


mx = df['subtlety'].astype('float').mean()


# In[41]:


df['subtlety'].replace(np.nan,mx,inplace =True)


# In[42]:


mx = df['size'].astype('float').mean()


# In[43]:


df['size'].replace(np.nan,mx,inplace =True)


# In[44]:


mx = df['x'].astype('float').mean()


# In[45]:


df['x'].replace(np.nan,mx,inplace =True)


# In[46]:


mx = df['y'].astype('float').mean()


# In[47]:


df['y'].replace(np.nan,mx,inplace =True)


# In[52]:


df['position'].value_counts().max()


# In[56]:


mx = df['position'].value_counts().idxmax()


# In[57]:


df['position'].replace(np.nan,mx,inplace =True)


# In[58]:


df['diagnosis'].value_counts().max()


# In[59]:


mx = df['diagnosis'].value_counts().idxmax()


# In[62]:


df['diagnosis'].replace(np.nan,mx,inplace =True)


# In[63]:


plt.pyplot.hist(df['diagnosis'], color = 'yellow',ec='black')


#
#
