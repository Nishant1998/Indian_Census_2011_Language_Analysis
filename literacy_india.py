#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # 1. Read Data
# ### Read census data

# In[2]:


c8 = pd.read_excel("Data/C08.xlsx",index_col=False)

# removing top 5 rows 
c8 = c8.drop([0,1,2,3,4,5])
new_header = range(0,45)
c8.columns = new_header
c8 = c8[[1,4,5,6,9,12,15,18,21,24,27,30,33,36,39,42]]
c8 = c8[(c8[5] == 'All ages') & (c8[4] == 'Total')]
c8 = c8.reset_index()
c8 = c8.drop(['index'], axis = 1)


c8.head(5)


# In[ ]:





# ###  Read C19

# In[3]:


c19 = pd.read_excel("Data/C19.xlsx",index_col=False)

# removing top 5 rows 
c19 = c19.drop([0,1,2,3,4,869,870,871])

# Adding new header
new_header = ['State_code','District_code','Area','TRU','Education_level','Persons_2','Males_2','Females_2','Persons_3','Males_3','Females_3']
c19.columns = new_header

#reset index
c19 = c19.reset_index()
c19 = c19.drop(['index'], axis = 1)


# # 2. For all state find education level with heighest percentage of people speaking 3 or more language

# In[4]:


stateCode = np.array(c8[1].to_list())
stateCode


# In[5]:


edu_level = c19.Education_level.unique()
edu_level


# In[6]:


literacy_india = pd.DataFrame(data=None, index=None,columns=['State/UT','Literacy_Group','Percentage'])


# In[7]:


# for India and all states
for i in range(0,36):
    # get c19 state wise data
    index = c19[(c19['State_code'] == stateCode[i]) & (c19['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c19.index,index)
    stateWiseData = c19.drop(notStateIndex, inplace = False)
    
    # get population
    List = c8[c8[1] == stateCode[i]].to_numpy()
    List = List[0]
    population = [List[3],List[4],List[5]+List[6]+List[15],List[7],List[8],List[9],List[10]+List[11]+List[12]+List[13],List[14]]

    
    
    # get people speaking 3 or more lang for all age group
    eduWiseCount = np.array(stateWiseData.Persons_3.to_list()[1:])
    percentage = eduWiseCount/population[1:]
    maxIndex = percentage.argsort()[-1:][0]
    
    
    # add in table
    literacy_india.loc[len(literacy_india.index)] = [i,edu_level[maxIndex+1],percentage[maxIndex]*100]
    
    


# In[ ]:





# In[ ]:





# # Save output file

# In[8]:


# Save output File
literacy_india.to_csv("Data/output/literacy_india.csv",index=False)


# In[8]:


literacy_india


# In[ ]:





# In[ ]:




