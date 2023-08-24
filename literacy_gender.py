#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd


# # 1. Read Data
# ### Read census data - c08

# In[16]:


c8 = pd.read_excel("Data/C08.xlsx",index_col=False)

# removing top 5 rows 
c8 = c8.drop([0,1,2,3,4,5])
new_header = range(0,45)
c8.columns = new_header
#c8 = c8[[1,4,5,6,9,12,15,18,21,24,27,30,33,36,39,42]]
c8 = c8[(c8[5] == 'All ages') & (c8[4] == 'Total')]
c8 = c8.reset_index()
c8 = c8.drop(['index'], axis = 1)


c8.head(5)


# ###  Read C19

# In[17]:


c19 = pd.read_excel("Data/C19.xlsx",index_col=False)

# removing top 5 rows 
c19 = c19.drop([0,1,2,3,4,869,870,871])

# Adding new header
new_header = ['State_code','District_code','Area','TRU','Education_level','Persons_2','Males_2','Females_2','Persons_3','Males_3','Females_3']
c19.columns = new_header

#reset index
c19 = c19.reset_index()
c19 = c19.drop(['index'], axis = 1)
c19


# # 2. For all state find education level with heighest percentage of people speaking 3 or more language

# In[18]:


stateCode = np.array(c8[1].to_list())
stateCode


# In[19]:


edu_level = c19.Education_level.unique()
edu_level


# In[ ]:





# In[20]:


# create empty dataframe
literacy_gender_3 = pd.DataFrame(data=None, index=None,columns=['State/UT','literacy_group_males','ratio_male','literacy_group_females','ratio_female'])
literacy_gender_2 = pd.DataFrame(data=None, index=None,columns=['State/UT','literacy_group_males','ratio_male','literacy_group_females','ratio_female'])
literacy_gender_1 = pd.DataFrame(data=None, index=None,columns=['State/UT','literacy_group_males','ratio_male','literacy_group_females','ratio_female'])


# In[21]:


# for India and all states
for i in range(0,36):
    # get c19 state wise data
    index = c19[(c19['State_code'] == stateCode[i]) & (c19['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c19.index,index)
    stateWiseData = c19.drop(notStateIndex, inplace = False)
    
     # get population
    List = c8[c8[1] == stateCode[0]].to_numpy()
    List = List[0]
    population_male = [List[7],List[10],List[13]+List[16]+List[43],List[19],List[22],List[25],List[28]+List[31]+List[34]+List[37],List[40]]
    population_female = [List[8],List[11],List[14]+List[17]+List[44],List[20],List[23],List[26],List[29]+List[32]+List[35]+List[38],List[41]]

    
    
    # get people speaking 3 or more lang for all age group
    eduWiseCountMale = np.array(stateWiseData.Males_3.to_list()[3:])
    eduWiseCountFemale = np.array(stateWiseData.Females_3.to_list()[3:])
    
    percentageMale = eduWiseCountMale/population_male[3:]
    percentageFemale = eduWiseCountFemale/population_female[3:]
    
    maxIndexMale = percentageMale.argsort()[-1:][0]
    maxIndexFemale = percentageFemale.argsort()[-1:][0]
    
    
    # add in table
    literacy_gender_3.loc[len(literacy_gender_3.index)] = [i,edu_level[maxIndexMale+3],percentageMale[maxIndexMale],edu_level[maxIndexFemale+3],percentageFemale[maxIndexFemale]]
    
    


# In[22]:


# for India and all states
for i in range(0,36):
    # get c19 state wise data
    index = c19[(c19['State_code'] == stateCode[i]) & (c19['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c19.index,index)
    stateWiseData = c19.drop(notStateIndex, inplace = False)
    
     # get population
    List = c8[c8[1] == stateCode[0]].to_numpy()
    List = List[0]
    population_male = [List[7],List[10],List[13]+List[16]+List[43],List[19],List[22],List[25],List[28]+List[31]+List[34]+List[37],List[40]]
    population_female = [List[8],List[11],List[14]+List[17]+List[44],List[20],List[23],List[26],List[29]+List[32]+List[35]+List[38],List[41]]

    
    
    # get people speaking 2  lang for all age group
    eduWiseCountMale = np.array(stateWiseData.Males_2.to_list()[3:]) - np.array(stateWiseData.Males_3.to_list()[3:])
    eduWiseCountFemale = np.array(stateWiseData.Females_2.to_list()[3:]) - np.array(stateWiseData.Females_3.to_list()[3:])
    
    percentageMale = eduWiseCountMale/population_male[3:]
    percentageFemale = eduWiseCountFemale/population_female[3:]
    
    maxIndexMale = percentageMale.argsort()[-1:][0]
    maxIndexFemale = percentageFemale.argsort()[-1:][0]
    
    
    # add in table
    literacy_gender_2.loc[len(literacy_gender_2.index)] = [i,edu_level[maxIndexMale+3],percentageMale[maxIndexMale],edu_level[maxIndexFemale+3],percentageFemale[maxIndexFemale]]
    
    


# In[23]:


# for India and all states
for i in range(0,36):
    # get c19 state wise data
    index = c19[(c19['State_code'] == stateCode[i]) & (c19['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c19.index,index)
    stateWiseData = c19.drop(notStateIndex, inplace = False)
    
     # get population
    List = c8[c8[1] == stateCode[0]].to_numpy()
    List = List[0]
    population_male = [List[7],List[10],List[13]+List[16]+List[43],List[19],List[22],List[25],List[28]+List[31]+List[34]+List[37],List[40]]
    population_female = [List[8],List[11],List[14]+List[17]+List[44],List[20],List[23],List[26],List[29]+List[32]+List[35]+List[38],List[41]]

    
    
    # get people speaking 2  lang for all age group
    eduWiseCountMale = population_male[3:]- np.array(stateWiseData.Males_2.to_list()[3:])
    eduWiseCountFemale = population_female[3:] -  np.array(stateWiseData.Females_2.to_list()[3:])
    
    percentageMale = eduWiseCountMale/population_male[3:]
    percentageFemale = eduWiseCountFemale/population_female[3:]
    
    maxIndexMale = percentageMale.argsort()[-1:][0]
    maxIndexFemale = percentageFemale.argsort()[-1:][0]
    
    
    # add in table
    literacy_gender_1.loc[len(literacy_gender_1.index)] = [i,edu_level[maxIndexMale+3],percentageMale[maxIndexMale],edu_level[maxIndexFemale+3],percentageFemale[maxIndexFemale]]
    
    


# In[24]:


# Save output File
literacy_gender_1.to_csv("Data/output/literacy_gender_a.csv",index=False)
literacy_gender_2.to_csv("Data/output/literacy_gender_b.csv",index=False)
literacy_gender_3.to_csv("Data/output/literacy_gender_c.csv",index=False)


# In[25]:


literacy_gender_3


# In[ ]:




