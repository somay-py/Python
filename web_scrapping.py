#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
response= requests.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')


# In[ ]:





# In[5]:


print(response)


# In[10]:



raw=BeautifulSoup(response.text,'html.parser')
print(raw)


# In[12]:


import pandas as pd


# In[14]:


data=pd.read_html('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')


# In[16]:


data


# In[18]:


data[0]


# In[20]:


main=data[0]
main.describe()


# In[36]:


main.to_csv('web_scrape.csv')


# In[ ]:




