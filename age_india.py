#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


#!pip install xlrd


# # 1. Read Data
# ### Read census data - c14

# In[3]:


c14 = pd.read_excel("Data/C14.xls",index_col=False)

# removing top 5 rows 
c14 = c14.drop([0,1,2,3,4,5])
new_header = ['A','state_code','C','D','age_group','total','G','H','I','J','K','L','M','N']
c14.columns = new_header
c14 = c14.drop(['A','C','D','G','H','I','J','K','L','M','N'], axis = 1)
c14 = c14.reset_index()
c14 = c14.drop(['index'], axis = 1)
c14.head(5)


# ###  Read C18

# In[4]:


c18 = pd.read_csv("Data/c18_modified.csv",index_col=False)


# # 2. For all state find age group with heighest percentage 

# In[5]:


# get all age group
age_Group = c18.Age_group.unique()
age_Group


# In[6]:


# get all state code
stateCode = c14.state_code.unique()
stateCode


# In[7]:


# make new empty data frame
age_india = pd.DataFrame(data=None, index=None,columns=['State/UT','Age Group','Percentage'])


# In[ ]:





# In[8]:


# for India and all states
for i in range(0,36):
    # get c18 state wise data
    index = c18[(c18['State_code'] == int(stateCode[i])) & (c18['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c18.index,index)
    stateWiseData = c18.drop(notStateIndex, inplace = False)
    
    # get age wise total population
    List = c14[c14['state_code'] == stateCode[i]].total.to_list()
    population = [List[0],List[2],List[3],List[4],List[5],List[6],np.array(List[7:11]).sum(), np.array(List[11:15]).sum(), np.array(List[15:18]).sum(),List[18]]

    
    
    # get people speaking 3 or more lang for all age group
    ageWiseCount = np.array(stateWiseData.Persons_3.to_list()[1:])
    ## find percent of perple speaking 3 or more in that age group
    percentage = ageWiseCount / population[1:]
    ## get age group with highest percentage.
    maxIndex = percentage.argsort()[-1:][0]
    
    # add in table
    age_india.loc[len(age_india.index)] = [i,age_Group[maxIndex+1],percentage[maxIndex]*100]


# # Save output file

# In[9]:


# Save output File
age_india.to_csv("Data/output/age_india.csv",index=False)


# In[10]:


age_india


# In[ ]:





# In[ ]:




