#!/usr/bin/env python
# coding: utf-8

# In[1]:


#hello there


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as pyo
import plotly.graph_objs as go

get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


ncseds_df = pd.read_csv("Ncseds.csv",low_memory = False)
clrcb_df = pd.read_csv("CLRCB.csv", low_memory = False)
sorcb_df = pd.read_csv("SORCB.csv", low_memory = False)
tercb_df = pd.read_csv("TERCB.csv", low_memory = False)
enertypes_df = pd.read_csv("Types.csv", low_memory = False)
enertypes2 = pd.read_csv("Types2.csv", low_memory = False)
cost = pd.read_csv("Cost.csv", low_memory = False)


# In[4]:


ncseds_df.head()


# In[5]:


ncseds_df.info


# In[6]:


ncseds_df.dtypes


# In[7]:


ncseds_df.columns


# In[8]:


ncseds_df.shape


# In[9]:


ncseds_df[ncseds_df['MSN']=='CLRCB']


# In[10]:


sns.set(rc={"figure.figsize":(10,3)})
sns.lineplot(data=clrcb_df, x ='Year', y='data', hue='CLRCB')
plt.savefig('coalusage.png', bbox_inches="tight", dpi=200)


# In[26]:


sns.set(rc={"figure.figsize":(10,3)})
sns.lineplot(data=sorcb_df, x ='Year', y='data', hue='SORCB')
plt.savefig('Solarenergyusage.png', bbox_inches="tight", dpi=200)


# In[12]:


sns.set(rc={"figure.figsize":(10,3)})
sns.lineplot(data=tercb_df, x ='Year', y='data', hue='TERCB')
plt.savefig('totalenergyusage.png', bbox_inches="tight", dpi=200)


# In[28]:


sns.lineplot(data=cost, x ='Year', y='data', hue='TERCD')
plt.savefig('totalenergycost.png', bbox_inches="tight", dpi=200)


# In[13]:


sns.set(rc={"figure.figsize":(10,5)})
sns.lineplot(data=enertypes_df)
plt.savefig('allenergyusage.png', bbox_inches="tight", dpi=200)


# In[19]:


energy_types = enertypes2.pivot("Year","Type", "Total")
energy_types.head()
sns.scatterplot(data=energy_types)
plt.savefig('yearlyenergyusage.png', bbox_inches="tight", dpi=200)


# In[24]:





# In[15]:


def msn_type(s):
    lookup = {
        1: "CLRCB",
        2: "DFRCB",
        3: "ESRCB",
        4: "SORCB"
    }
    if s not in lookup:
        return "other"
    else:
        return lookup[s]



# In[ ]:




