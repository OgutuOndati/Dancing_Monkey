#!/usr/bin/env python
# coding: utf-8

# In[1]:


import camelot as cm


# In[ ]:





# In[4]:


input_pdf = cm.read_pdf("C:\\Users\\gf\\Desktop\\Automation\\india_factsheet_economic_n_hdi.pdf")


# In[5]:


input_pdf


# In[7]:


for n in input_pdf:
    print(n)


# In[8]:


input_pdf[1].df


# In[9]:


df = input_pdf[1].df.loc[8:14, 0:2]
df


# In[10]:


df = df.reset_index(drop= True)


# In[11]:


df.columns = ["KPI","2001","2011"]


# In[12]:


df


# In[15]:


df.drop([0,2,6], axis=0, inplace=True)
df


# In[16]:


df.drop([5],axis=0,inplace=True)


# In[17]:


df


# In[18]:


df.loc[:,["2001","2011"]] = df.loc[:,["2001","2011"]].astype(float)


# In[19]:


df


# In[20]:


df.to_csv("FactIndia.csv")


# In[22]:


df


# In[27]:


df.to_excel("FactIndia.xlsx")


# In[ ]:





# In[25]:


import pandas as pd


# In[28]:


df2 = pd.read_csv("FactIndia.csv")


# In[29]:


df2


# In[30]:


import seaborn as sns


# In[31]:


df_melted = df.melt('KPI', var_name='year', value_name='percentage')


# In[32]:


df_melted


# In[40]:


sns.barplot(x= 'KPI', y = 'percentage',hue = 'year', data = df_melted);


# In[ ]:




