#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# ## Reading Data
# ### Reading census data

# In[2]:


censusData = pd.read_csv("Data/CensusData.csv",low_memory=False,index_col=False)
censusData.head(5)


# ### Reading c18 Data

# In[3]:


c18 = pd.read_excel("Data/C18.xlsx",index_col=False)
c18.head(5)


# In[4]:


# removing top 5 rows 
c18 = c18.drop([0,1,2,3,4])


# In[5]:


# Adding new header
new_header = ['State_code','District_code','Area','TRU','Age_group','Persons_2','Males_2','Females_2','Persons_3','Males_3','Females_3']
c18.columns = new_header


# In[6]:


#reset index
c18 = c18.reset_index()
c18 = c18.drop(['index'], axis = 1)
c18.head(3)


# ## Get required data from dataframe

# In[7]:


# total population of india
totalPopulation = censusData.iloc[0][10]

# Total person speaking 2 and 3 language in india
secoundLang =  c18.iloc[0][5]
thirdLang = c18.iloc[0][8]
secoundLang = secoundLang - thirdLang

# Tatal person speaking only one language
firstLang = totalPopulation - (secoundLang + thirdLang)


# In[8]:


# get census data of state
stateCensus = censusData[ (censusData['Level'] == 'STATE') & (censusData['TRU'] == 'Total')] 
stateTotalPopulation = np.array(stateCensus.TOT_P.to_list())

# get nuber of ppeople speaking 1,2,3 lang in states
stateLang = c18[ (c18['Age_group'] == 'Total') & (c18['TRU'] == 'Total') & (c18['State_code'] != '00')] 
stateLang.Area.to_list()

stateLang2 = np.array(stateLang.Persons_2.to_list())
stateLang3 = np.array(stateLang.Persons_3.to_list())
stateLang2 = stateLang2 - stateLang3
  
stateLang1 = stateTotalPopulation - (stateLang2 + stateLang3)


# ## Calculate percentage

# In[9]:


# calculate percent for india
oneLangPercent = firstLang/totalPopulation
twoLangPercent = secoundLang/totalPopulation
threeLangPercent = thirdLang/totalPopulation


# In[10]:


# calculate for states
stateOneLangPercent = stateLang1/stateTotalPopulation
stateTwoLangPercent = stateLang2/stateTotalPopulation
stateThreeLangPercent = stateLang3/stateTotalPopulation


# In[16]:


data = {'state_code': np.array(range(1,36)), 
        'percent_one' : stateOneLangPercent*100, 'percent_two':stateTwoLangPercent*100 , 
        ' percent_three' :stateThreeLangPercent*100 }


# In[17]:


# new dataframe
percent_india = pd.DataFrame(data)
percent_india.loc[len(percent_india.index)] = [0, oneLangPercent*100, twoLangPercent*100, threeLangPercent*100]
percent_india = percent_india.sort_values('state_code')


# In[18]:


# Save output File
percent_india.to_csv("Data/output/percent_india.csv",index=False)


# In[19]:


# Save modified c18 
c18.to_csv("Data/c18_modified.csv",index=False)


# In[20]:


percent_india


# In[ ]:





# In[ ]:




