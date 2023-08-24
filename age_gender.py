#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # 1. Read Data
# ### Read census data - C14

# In[2]:


c14 = pd.read_excel("Data/C14.xls",index_col=False)

# removing top 5 rows 
c14 = c14.drop([0,1,2,3,4,5])
new_header = ['A','state_code','C','D','age_group','total','males','females','I','J','K','L','M','N']
c14.columns = new_header
c14 = c14.drop(['A','C','D','I','J','K','L','M','N'], axis = 1)
c14 = c14.reset_index()
c14 = c14.drop(['index'], axis = 1)
c14.head(5)


# ###  Read C18

# In[3]:


c18 = pd.read_csv("Data/c18_modified.csv",index_col=False)


# # 2. For all state find age group with heighest percentage 

# In[4]:


# get all age group
age_Group = c18.Age_group.unique()
age_Group


# In[5]:


# get all state code
stateCode = c14.state_code.unique()
stateCode


# In[6]:


# make new empty data frame
age_gender_3 = pd.DataFrame(data=None, index=None,columns=['State/UT','age_group_males','ratio_of_3_male','age_group_females','ratio_of_3_female'])
age_gender_2 = pd.DataFrame(data=None, index=None,columns=['State/UT','age_group_males','ratio_of_2_male','age_group_females','ratio_of_2_female'])
age_gender_1 = pd.DataFrame(data=None, index=None,columns=['State/UT','age_group_males','ratio_of_1_male','age_group_females','ratio_of_1_female'])


# In[7]:


# for India and all states
for i in range(0,36):
    # get c18 state wise data
    index = c18[(c18['State_code'] == int(stateCode[i])) & (c18['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c18.index,index)
    stateWiseData = c18.drop(notStateIndex, inplace = False)
    
   # get age wise total population
    list_male = c14[c14['state_code'] == stateCode[i]].males.to_list()
    list_female = c14[c14['state_code'] == stateCode[i]].females.to_list()
    population_male = [list_male[0],list_male[2],list_male[3],list_male[4],list_male[5],list_male[6],np.array(list_male[7:11]).sum(), np.array(list_male[11:15]).sum(), np.array(list_male[15:18]).sum(),list_male[18]]
    population_female = [list_female[0],list_female[2],list_female[3],list_female[4],list_female[5],list_female[6],np.array(list_female[7:11]).sum(), np.array(list_female[11:15]).sum(), np.array(list_female[15:18]).sum(),list_female[18]]

    
    
    # get people speaking 3 or more lang for all age group
    ageWiseCountMale = np.array(stateWiseData.Males_3.to_list()[1:])
    ageWiseCountFemale = np.array(stateWiseData.Females_3.to_list()[1:])
    ## find percent of perple speaking 3 or more in that age group
    percentageMale = ageWiseCountMale / population_male[1:]
    percentageFemale = ageWiseCountFemale / population_female[1:]
    ## get age group with highest percentage.
    maxIndexMale = percentageMale.argsort()[-1:][0]
    maxIndexFemale = percentageFemale.argsort()[-1:][0]
    
    # add in table
    age_gender_3.loc[len(age_gender_3.index)] = [i,age_Group[maxIndexMale+1],percentageMale[maxIndexMale],age_Group[maxIndexFemale+1],percentageFemale[maxIndexFemale]]


# In[8]:


# for India and all states
for i in range(0,36):
    # get c18 state wise data
    index = c18[(c18['State_code'] == int(stateCode[i])) & (c18['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c18.index,index)
    stateWiseData = c18.drop(notStateIndex, inplace = False)
    
   # get age wise total population
    list_male = c14[c14['state_code'] == stateCode[i]].males.to_list()
    list_female = c14[c14['state_code'] == stateCode[i]].females.to_list()
    population_male = [list_male[0],list_male[2],list_male[3],list_male[4],list_male[5],list_male[6],np.array(list_male[7:11]).sum(), np.array(list_male[11:15]).sum(), np.array(list_male[15:18]).sum(),list_male[18]]
    population_female = [list_female[0],list_female[2],list_female[3],list_female[4],list_female[5],list_female[6],np.array(list_female[7:11]).sum(), np.array(list_female[11:15]).sum(), np.array(list_female[15:18]).sum(),list_female[18]]

    
    
    # get people speaking 3 or more lang for all age group
    ageWiseCountMale = np.array(stateWiseData.Males_2.to_list()[1:]) - np.array(stateWiseData.Males_3.to_list()[1:])
    ageWiseCountFemale = np.array(stateWiseData.Females_2.to_list()[1:]) - np.array(stateWiseData.Females_3.to_list()[1:])
    ## find percent of perple speaking 3 or more in that age group
    percentageMale = ageWiseCountMale / population_male[1:]
    percentageFemale = ageWiseCountFemale / population_female[1:]
    ## get age group with highest percentage.
    maxIndexMale = percentageMale.argsort()[-1:][0]
    maxIndexFemale = percentageFemale.argsort()[-1:][0]
    
    # add in table
    age_gender_2.loc[len(age_gender_2.index)] = [i,age_Group[maxIndexMale+1],percentageMale[maxIndexMale],age_Group[maxIndexFemale+1],percentageFemale[maxIndexFemale]]


# In[9]:


# for India and all states
for i in range(0,36):
    # get c18 state wise data
    index = c18[(c18['State_code'] == int(stateCode[i])) & (c18['TRU'] == 'Total')].index
    notStateIndex = np.setdiff1d(c18.index,index)
    stateWiseData = c18.drop(notStateIndex, inplace = False)
    
   # get age wise total population
    list_male = c14[c14['state_code'] == stateCode[i]].males.to_list()
    list_female = c14[c14['state_code'] == stateCode[i]].females.to_list()
    population_male = [list_male[0],list_male[2],list_male[3],list_male[4],list_male[5],list_male[6],np.array(list_male[7:11]).sum(), np.array(list_male[11:15]).sum(), np.array(list_male[15:18]).sum(),list_male[18]]
    population_female = [list_female[0],list_female[2],list_female[3],list_female[4],list_female[5],list_female[6],np.array(list_female[7:11]).sum(), np.array(list_female[11:15]).sum(), np.array(list_female[15:18]).sum(),list_female[18]]

    
    
    # get people speaking 3 or more lang for all age group
    ageWiseCountMale = population_male[1:] - np.array(stateWiseData.Males_2.to_list()[1:])
    ageWiseCountFemale = population_female[1:] - np.array(stateWiseData.Females_2.to_list()[1:])
    ## find percent of perple speaking 3 or more in that age group
    percentageMale = ageWiseCountMale / population_male[1:]
    percentageFemale = ageWiseCountFemale / population_female[1:]
    ## get age group with highest percentage.
    maxIndexMale = percentageMale.argsort()[-1:][0]
    maxIndexFemale = percentageFemale.argsort()[-1:][0]
    
    # add in table
    age_gender_1.loc[len(age_gender_1.index)] = [i,age_Group[maxIndexMale+1],percentageMale[maxIndexMale],age_Group[maxIndexFemale+1],percentageFemale[maxIndexFemale]]


# In[10]:


# Save output File
age_gender_1.to_csv("Data/output/age_gender_c.csv",index=False)
age_gender_2.to_csv("Data/output/age_gender_b.csv",index=False)
age_gender_3.to_csv("Data/output/age_gender_a.csv",index=False)


# In[12]:





# In[ ]:




