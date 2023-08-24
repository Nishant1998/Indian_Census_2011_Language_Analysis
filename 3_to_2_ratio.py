#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # 1. Read Data
# ### Read census data

# In[2]:


censusData = pd.read_csv("Data/CensusData.csv",low_memory=False,index_col=False)
censusData.head(5)


# ###  Read C18

# In[3]:


c18 = pd.read_csv("Data/c18_modified.csv",index_col=False)


# # 2. Get population for all state

# In[4]:


stateCode = c18.State_code.unique()
Population_List = []
state_Names = []
for i in range(1,36):
    # get census state wise data
    index = censusData[(censusData['State'] == int(stateCode[i])) & (censusData['Level'] == 'STATE')  &  (censusData['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(censusData.index,index)
    stateWiseCensusData = censusData.drop(notStateIndex, inplace = False)
    Population = int(stateWiseCensusData['TOT_P'])
    
    Population_List.append(Population)
    state_Names.append(stateWiseCensusData.Name.to_list()[0])


# # 3. Get Number of people speaking 2 and 3 languages

# In[5]:


c18.head(3)


# In[6]:


lang2_List = []
lang3_List = []
for i in range(1,36):
    # get census state wise data
    index = c18[(c18['State_code'] == int(stateCode[i])) & (c18['TRU'] == 'Total') & (c18['Age_group'] == 'Total')].index
    notStateIndex = np.setdiff1d(c18.index,index)
    stateWiseData = c18.drop(notStateIndex, inplace = False)
    lang2 = int(stateWiseData['Persons_2'])
    lang3 = int(stateWiseData['Persons_3'])
    
    ''' if 2 or more then '''
    lang2 = lang2 - lang3
    
    lang2_List.append(lang2)
    lang3_List.append(lang3)


# # 4. Find ratio
# ## Ratio of only 2 language to population

# In[7]:


ratio_lang2 = np.array(lang2_List)/np.array(Population_List)


# ## Ratio of 3 for more language to population

# In[8]:


ratio_lang3 = np.array(lang3_List)/np.array(Population_List)


# ## Ratio of 3 to 2 language

# In[9]:


ratio = np.array(ratio_lang3)/np.array(ratio_lang2)


# # 5. get state code of top 3 and bottom 3 state

# In[10]:


top3_index = ratio.argsort()[-3:][::-1]
worst3_index = ratio.argsort()[:3]


# # 6. Save ratio in file

# In[11]:


# new dataframe
_3_to_2_ratio = pd.DataFrame(data=None, index=None,columns=['Name','ratio'])
# add data in dataframe
_3_to_2_ratio.loc[len(_3_to_2_ratio.index)] = [state_Names[top3_index[0]],ratio[top3_index[0]]]
_3_to_2_ratio.loc[len(_3_to_2_ratio.index)] = [state_Names[top3_index[1]],ratio[top3_index[1]]] 
_3_to_2_ratio.loc[len(_3_to_2_ratio.index)] = [state_Names[top3_index[2]],ratio[top3_index[2]]] 

_3_to_2_ratio.loc[len(_3_to_2_ratio.index)] = [state_Names[worst3_index[0]],ratio[worst3_index[0]]]
_3_to_2_ratio.loc[len(_3_to_2_ratio.index)] = [state_Names[worst3_index[1]],ratio[worst3_index[1]]] 
_3_to_2_ratio.loc[len(_3_to_2_ratio.index)] = [state_Names[worst3_index[2]],ratio[worst3_index[2]]] 


# In[12]:


# Save output File
_3_to_2_ratio.to_csv("Data/output/3_to_2_ratio.csv",index=False)


# In[14]:


_3_to_2_ratio


# In[ ]:





# In[ ]:




