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


# # 3. Get Number of people speaking 1 and 2 languages

# In[5]:


c18.head(3)


# In[ ]:





# In[6]:


lang1_List = []
lang2_List = []
for i in range(1,36):
    # get c18 state wise data
    index = c18[(c18['State_code'] == int(stateCode[i])) & (c18['TRU'] == 'Total') & (c18['Age_group'] == 'Total')].index
    notStateIndex = np.setdiff1d(c18.index,index)
    stateWiseData = c18.drop(notStateIndex, inplace = False)
    lang2 = int(stateWiseData['Persons_2'])
    lang3 = int(stateWiseData['Persons_3'])
    
    ''' if 2 or more then '''
    lang2 = lang2 - lang3
    
    lang1 = Population_List[i-1] - (lang2 + lang3)
    
    if i == 30:
        print(lang2)
        print(lang3)
    
    lang1_List.append(lang1)
    lang2_List.append(lang2)


# # 4. Find ratio
# ## Ratio of only 1 language to population

# In[7]:


ratio_lang1 = np.array(lang1_List)/np.array(Population_List)


# ## Ratio of 2 for more language to population

# In[8]:


ratio_lang2 = np.array(lang2_List)/np.array(Population_List)


# ## Ratio of 2 to 1 language

# In[9]:


ratio = np.array(ratio_lang2)/np.array(ratio_lang1)


# # 5. get state code of top 3 and bottom 3 state

# In[10]:


top3_index = ratio.argsort()[-3:][::-1]
worst3_index = ratio.argsort()[:3]


# # 6. Save ratio in file

# In[11]:


# new dataframe
_2_to_1_ratio = pd.DataFrame(data=None, index=None,columns=['Name','ratio'])
# add data in dataframe
_2_to_1_ratio.loc[len(_2_to_1_ratio.index)] = [state_Names[top3_index[0]],ratio[top3_index[0]]]
_2_to_1_ratio.loc[len(_2_to_1_ratio.index)] = [state_Names[top3_index[1]],ratio[top3_index[1]]] 
_2_to_1_ratio.loc[len(_2_to_1_ratio.index)] = [state_Names[top3_index[2]],ratio[top3_index[2]]] 

_2_to_1_ratio.loc[len(_2_to_1_ratio.index)] = [state_Names[worst3_index[0]],ratio[worst3_index[0]]]
_2_to_1_ratio.loc[len(_2_to_1_ratio.index)] = [state_Names[worst3_index[1]],ratio[worst3_index[1]]] 
_2_to_1_ratio.loc[len(_2_to_1_ratio.index)] = [state_Names[worst3_index[2]],ratio[worst3_index[2]]] 


# In[12]:


# Save output File
_2_to_1_ratio.to_csv("Data/output/2_to_1_ratio.csv",index=False)


# In[13]:


_2_to_1_ratio

