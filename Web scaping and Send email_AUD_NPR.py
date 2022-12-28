#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import bs4
import smtplib


# In[10]:


url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=AUD&To=NPR'


# In[11]:


page = requests.get(url)


# In[12]:


page.text


# In[13]:


html = page.content


# In[17]:


html = soup.find('p',{'class':'result__BigRate-sc-1bsijpp-1 iGrAod'}).text


# In[18]:


html


# #### SENDING EMAIL

# In[ ]:





# In[49]:


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()


# In[50]:


server.login('romishkrishnashrestha@gmail.com','Kathmandu1983')


# In[57]:


email = 'romishkrishnashrestha@gmail.com'


# In[55]:


message = '''Hi Romish and Suprina,

Today the exchange rate for Nepalese Rupees to Australian Dollar is: 

1 AUD = ''' + html +'''


Sent from Python'''


# In[56]:


message


# In[53]:


tolist = ['romishshrestha@gmail.com','suprinabasnyat@gmail.com']


# In[54]:


server.sendmail(from_addr=email, to_addrs= tolist, msg = message)


# In[ ]:


server.quit()

