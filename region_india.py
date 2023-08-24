#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
from collections import Counter


# In[19]:


# set region 
North = [1, 2, 3, 4, 5, 6, 7]
West= [ 8, 24, 25, 26, 27, 30]
Central = [ 9, 22, 23]
East = [10, 19, 20, 21]
South = [28, 29, 31, 32, 33, 34]
North_East = [11, 12, 13, 14, 15, 16, 17, 18, 35]

# c17 folder file name
c17_file = ['DDW-C17-0100.XLSX', 'DDW-C17-0200.XLSX', 'DDW-C17-0300.XLSX', 'DDW-C17-0400.XLSX', 'DDW-C17-0500.XLSX', 'DDW-C17-0600.XLSX', 'DDW-C17-0700.XLSX', 'DDW-C17-0800.XLSX', 'DDW-C17-0900.XLSX', 'DDW-C17-1000.XLSX', 'DDW-C17-1100.XLSX', 'DDW-C17-1200.XLSX', 'DDW-C17-1300.XLSX', 'DDW-C17-1400.XLSX', 'DDW-C17-1500.XLSX', 'DDW-C17-1600.XLSX', 'DDW-C17-1700.XLSX', 'DDW-C17-1800.XLSX', 'DDW-C17-1900.XLSX', 'DDW-C17-2000.XLSX','DDW-C17-2100.XLSX', 'DDW-C17-2200.XLSX', 'DDW-C17-2300.XLSX', 'DDW-C17-2400.XLSX', 'DDW-C17-2500.XLSX', 'DDW-C17-2600.XLSX', 'DDW-C17-2700.XLSX', 'DDW-C17-2800.XLSX', 'DDW-C17-2900.XLSX', 'DDW-C17-3000.XLSX', 'DDW-C17-3100.XLSX', 'DDW-C17-3200.XLSX', 'DDW-C17-3300.XLSX', 'DDW-C17-3400.XLSX', 'DDW-C17-3500.XLSX']
#import os
#os.listdir("./data/C17")


# ## Get all Language Names

# In[20]:


c17 = pd.read_excel("Data/C17.xlsx",index_col=False)
# removing top 5 rows 
c17 = c17.drop([0,1,2,3,4])

# Adding new header
new_header = ['State_code','State_name','Code','Name','Persons','Males','Females','Code_1','Name_1','Persons_1','Males_1','Females_1','Code_2','Name_2','Persons_2','Males_2','Females_2']
c17.columns = new_header
#reset index
c17 = c17.reset_index()
c17 = c17.drop(['index'], axis = 1)
c17 = c17[c17.Code.notna()]

language_Names = np.array(c17.Name.to_list())


# In[ ]:





# ### 1. For North Region

# In[21]:


dict_a = {}
dict_b= {}
# for north region
for i in North:
    fileName = c17_file[i-1]
    path = "Data/C17/" + fileName
    c17_stateWise = pd.read_excel(path,index_col=False)
    
    # removing top 5 rows 
    c17_stateWise = c17_stateWise.drop([0,1,2,3,4])

    # Adding new header
    new_header = ['State_code','State_name','Code','Name','Persons','Males','Females','Code_1','Name_1','Persons_1','Males_1','Females_1','Code_2','Name_2','Persons_2','Males_2','Females_2']
    c17_stateWise.columns = new_header
    
    # Get speakers of not mother tongue speakers
    secondLang = c17_stateWise.iloc[:,[8,9]]
    secondLang = secondLang[secondLang.Name_1.notna()]
    secondDict = dict(zip(secondLang.Name_1.to_list(),secondLang.Persons_1.to_list()))

    thirdLang = c17_stateWise.iloc[:,[13,14]]
    thirdLang = thirdLang[thirdLang.Name_2.notna()]
    thirdDict = dict(zip(thirdLang.Name_2.to_list(),thirdLang.Persons_2.to_list()))
    # dictionary of  2nd language + 3rd language speakers
    secondAndThirdDict = dict(Counter(secondDict)+Counter(thirdDict))
    
    # remove null entery
    c17_stateWise.Code.notna()
    c17_stateWise = c17_stateWise[c17_stateWise.Code.notna()]
    
    # language speaker count
    langSpeakerCountDict = dict(zip(c17_stateWise.Name.to_list(),c17_stateWise.Persons.to_list()))
    
    # add count for region
    dict_a = Counter(dict_a) + Counter(langSpeakerCountDict)
    dict_b= Counter(dict_b) + Counter(secondAndThirdDict) + Counter(langSpeakerCountDict)

    
NorthMostCommon_a = Counter(dict_a).most_common(3)   
NorthMostCommon_b = Counter(dict_b).most_common(3)  


# ### 2. For West Region

# In[22]:


dict_a = {}
dict_b= {}
# for West region
for i in West:
    fileName = c17_file[i-1]
    path = "Data/C17/" + fileName
    c17_stateWise = pd.read_excel(path,index_col=False)
    
    # removing top 5 rows 
    c17_stateWise = c17_stateWise.drop([0,1,2,3,4])

    # Adding new header
    new_header = ['State_code','State_name','Code','Name','Persons','Males','Females','Code_1','Name_1','Persons_1','Males_1','Females_1','Code_2','Name_2','Persons_2','Males_2','Females_2']
    c17_stateWise.columns = new_header
    
    # Get speakers of not mother tongue speakers
    secondLang = c17_stateWise.iloc[:,[8,9]]
    secondLang = secondLang[secondLang.Name_1.notna()]
    secondDict = dict(zip(secondLang.Name_1.to_list(),secondLang.Persons_1.to_list()))

    thirdLang = c17_stateWise.iloc[:,[13,14]]
    thirdLang = thirdLang[thirdLang.Name_2.notna()]
    thirdDict = dict(zip(thirdLang.Name_2.to_list(),thirdLang.Persons_2.to_list()))
    # dictionary of  2nd language + 3rd language speakers
    secondAndThirdDict = dict(Counter(secondDict)+Counter(thirdDict))
    
    # remove null entery
    c17_stateWise.Code.notna()
    c17_stateWise = c17_stateWise[c17_stateWise.Code.notna()]
    
    # language speaker count
    langSpeakerCountDict = dict(zip(c17_stateWise.Name.to_list(),c17_stateWise.Persons.to_list()))
    
    # add count for region
    dict_a = Counter(dict_a) + Counter(langSpeakerCountDict)
    dict_b= Counter(dict_b) + Counter(secondAndThirdDict) + Counter(langSpeakerCountDict)

WestMostCommon_a = Counter(dict_a).most_common(3)   
WestMostCommon_b = Counter(dict_b).most_common(3)   


# ### 3. For Central Region

# In[23]:


dict_a = {}
dict_b= {}
# for Central region
for i in Central:
    fileName = c17_file[i-1]
    path = "Data/C17/" + fileName
    c17_stateWise = pd.read_excel(path,index_col=False)
    
    # removing top 5 rows 
    c17_stateWise = c17_stateWise.drop([0,1,2,3,4])

    # Adding new header
    new_header = ['State_code','State_name','Code','Name','Persons','Males','Females','Code_1','Name_1','Persons_1','Males_1','Females_1','Code_2','Name_2','Persons_2','Males_2','Females_2']
    c17_stateWise.columns = new_header
    
    # Get speakers of not mother tongue speakers
    secondLang = c17_stateWise.iloc[:,[8,9]]
    secondLang = secondLang[secondLang.Name_1.notna()]
    secondDict = dict(zip(secondLang.Name_1.to_list(),secondLang.Persons_1.to_list()))

    thirdLang = c17_stateWise.iloc[:,[13,14]]
    thirdLang = thirdLang[thirdLang.Name_2.notna()]
    thirdDict = dict(zip(thirdLang.Name_2.to_list(),thirdLang.Persons_2.to_list()))
    # dictionary of  2nd language + 3rd language speakers
    secondAndThirdDict = dict(Counter(secondDict)+Counter(thirdDict))
    
    # remove null entery
    c17_stateWise.Code.notna()
    c17_stateWise = c17_stateWise[c17_stateWise.Code.notna()]
    
    # language speaker count
    langSpeakerCountDict = dict(zip(c17_stateWise.Name.to_list(),c17_stateWise.Persons.to_list()))
    
    # add count for region
    dict_a = Counter(dict_a) + Counter(langSpeakerCountDict)
    dict_b= Counter(dict_b) + Counter(secondAndThirdDict) + Counter(langSpeakerCountDict)
    
    
CentralMostCommon_a = Counter(dict_a).most_common(3)   
CentralMostCommon_b = Counter(dict_b).most_common(3)   


# ### 4. For East Region

# In[24]:


dict_a = {}
dict_b= {}
# for East region
for i in East:
    fileName = c17_file[i-1]
    path = "Data/C17/" + fileName
    c17_stateWise = pd.read_excel(path,index_col=False)
    
    # removing top 5 rows 
    c17_stateWise = c17_stateWise.drop([0,1,2,3,4])

    # Adding new header
    new_header = ['State_code','State_name','Code','Name','Persons','Males','Females','Code_1','Name_1','Persons_1','Males_1','Females_1','Code_2','Name_2','Persons_2','Males_2','Females_2']
    c17_stateWise.columns = new_header
    
    # Get speakers of not mother tongue speakers
    secondLang = c17_stateWise.iloc[:,[8,9]]
    secondLang = secondLang[secondLang.Name_1.notna()]
    secondDict = dict(zip(secondLang.Name_1.to_list(),secondLang.Persons_1.to_list()))

    thirdLang = c17_stateWise.iloc[:,[13,14]]
    thirdLang = thirdLang[thirdLang.Name_2.notna()]
    thirdDict = dict(zip(thirdLang.Name_2.to_list(),thirdLang.Persons_2.to_list()))
    # dictionary of  2nd language + 3rd language speakers
    secondAndThirdDict = dict(Counter(secondDict)+Counter(thirdDict))
    
    # remove null entery
    c17_stateWise.Code.notna()
    c17_stateWise = c17_stateWise[c17_stateWise.Code.notna()]
    
    # language speaker count
    langSpeakerCountDict = dict(zip(c17_stateWise.Name.to_list(),c17_stateWise.Persons.to_list()))
    
    # add count for region
    dict_a = Counter(dict_a) + Counter(langSpeakerCountDict)
    dict_b= Counter(dict_b) + Counter(secondAndThirdDict) + Counter(langSpeakerCountDict)
    
    
EastMostCommon_a = Counter(dict_a).most_common(3)   
EastMostCommon_b = Counter(dict_b).most_common(3)  


# ### 5. For South Region

# In[25]:


dict_a = {}
dict_b= {}
# for South region
for i in South:
    fileName = c17_file[i-1]
    path = "Data/C17/" + fileName
    c17_stateWise = pd.read_excel(path,index_col=False)
    
    # removing top 5 rows 
    c17_stateWise = c17_stateWise.drop([0,1,2,3,4])

    # Adding new header
    new_header = ['State_code','State_name','Code','Name','Persons','Males','Females','Code_1','Name_1','Persons_1','Males_1','Females_1','Code_2','Name_2','Persons_2','Males_2','Females_2']
    c17_stateWise.columns = new_header
    
    # Get speakers of not mother tongue speakers
    secondLang = c17_stateWise.iloc[:,[8,9]]
    secondLang = secondLang[secondLang.Name_1.notna()]
    secondDict = dict(zip(secondLang.Name_1.to_list(),secondLang.Persons_1.to_list()))

    thirdLang = c17_stateWise.iloc[:,[13,14]]
    thirdLang = thirdLang[thirdLang.Name_2.notna()]
    thirdDict = dict(zip(thirdLang.Name_2.to_list(),thirdLang.Persons_2.to_list()))
    # dictionary of  2nd language + 3rd language speakers
    secondAndThirdDict = dict(Counter(secondDict)+Counter(thirdDict))
    
    # remove null entery
    c17_stateWise.Code.notna()
    c17_stateWise = c17_stateWise[c17_stateWise.Code.notna()]
    
    # language speaker count
    langSpeakerCountDict = dict(zip(c17_stateWise.Name.to_list(),c17_stateWise.Persons.to_list()))
    
    # add count for region
    dict_a = Counter(dict_a) + Counter(langSpeakerCountDict)
    dict_b= Counter(dict_b) + Counter(secondAndThirdDict) + Counter(langSpeakerCountDict)
    
    
SouthMostCommon_a = Counter(dict_a).most_common(3)   
SouthMostCommon_b = Counter(dict_b).most_common(3) 


# ### 6. For North_East Region

# In[26]:


dict_a = {}
dict_b= {}
# for North_East region
for i in North_East:
    fileName = c17_file[i-1]
    path = "Data/C17/" + fileName
    c17_stateWise = pd.read_excel(path,index_col=False)
    
    # removing top 5 rows 
    c17_stateWise = c17_stateWise.drop([0,1,2,3,4])

    # Adding new header
    new_header = ['State_code','State_name','Code','Name','Persons','Males','Females','Code_1','Name_1','Persons_1','Males_1','Females_1','Code_2','Name_2','Persons_2','Males_2','Females_2']
    c17_stateWise.columns = new_header
    
    # Get speakers of not mother tongue speakers
    secondLang = c17_stateWise.iloc[:,[8,9]]
    secondLang = secondLang[secondLang.Name_1.notna()]
    secondDict = dict(zip(secondLang.Name_1.to_list(),secondLang.Persons_1.to_list()))

    thirdLang = c17_stateWise.iloc[:,[13,14]]
    thirdLang = thirdLang[thirdLang.Name_2.notna()]
    thirdDict = dict(zip(thirdLang.Name_2.to_list(),thirdLang.Persons_2.to_list()))
    # dictionary of  2nd language + 3rd language speakers
    secondAndThirdDict = dict(Counter(secondDict)+Counter(thirdDict))
    
    # remove null entery
    c17_stateWise.Code.notna()
    c17_stateWise = c17_stateWise[c17_stateWise.Code.notna()]
    
    # language speaker count
    langSpeakerCountDict = dict(zip(c17_stateWise.Name.to_list(),c17_stateWise.Persons.to_list()))
    
    # add count for region
    dict_a = Counter(dict_a) + Counter(langSpeakerCountDict)
    dict_b = Counter(dict_b) + Counter(secondAndThirdDict) + Counter(langSpeakerCountDict)
    
    
NorthEastMostCommon_a = Counter(dict_a).most_common(3)   
NorthEastMostCommon_b = Counter(dict_b).most_common(3)   


# In[27]:


# mother tongue 
# make dataframe
region_india_a = pd.DataFrame(data=None, index=None,columns=['region', 'language_1', 'language_2', 'language_3'])

# add data in dataframe

region_india_a.loc[len(region_india_a.index)] = ['North',NorthMostCommon_a[0][0],NorthMostCommon_a[1][0],NorthMostCommon_a[2][0]]
region_india_a.loc[len(region_india_a.index)] = ['West',WestMostCommon_a[0][0],WestMostCommon_a[1][0],WestMostCommon_a[2][0]]
region_india_a.loc[len(region_india_a.index)] = ['Central',CentralMostCommon_a[0][0],CentralMostCommon_a[1][0],CentralMostCommon_a[2][0]]
region_india_a.loc[len(region_india_a.index)] = ['East',EastMostCommon_a[0][0],EastMostCommon_a[1][0],EastMostCommon_a[2][0]]
region_india_a.loc[len(region_india_a.index)] = ['South',SouthMostCommon_a[0][0],SouthMostCommon_a[1][0],SouthMostCommon_a[2][0]]
region_india_a.loc[len(region_india_a.index)] = ['North_East',NorthEastMostCommon_a[0][0],NorthEastMostCommon_a[1][0],NorthEastMostCommon_a[2][0]]


# In[28]:


# mother tongue + 2nd language + 3rd language.
# make dataframe
region_india_b = pd.DataFrame(data=None, index=None,columns=['region', 'language_1', 'language_2', 'language_3'])

# add data in dataframe

region_india_b.loc[len(region_india_b.index)] = ['North',NorthMostCommon_b[0][0],NorthMostCommon_b[1][0],NorthMostCommon_b[2][0]]
region_india_b.loc[len(region_india_b.index)] = ['West',WestMostCommon_b[0][0],WestMostCommon_b[1][0],WestMostCommon_b[2][0]]
region_india_b.loc[len(region_india_b.index)] = ['Central',CentralMostCommon_b[0][0],CentralMostCommon_b[1][0],CentralMostCommon_b[2][0]]
region_india_b.loc[len(region_india_b.index)] = ['East',EastMostCommon_b[0][0],EastMostCommon_b[1][0],EastMostCommon_b[2][0]]
region_india_b.loc[len(region_india_b.index)] = ['South',SouthMostCommon_b[0][0],SouthMostCommon_b[1][0],SouthMostCommon_b[2][0]]
region_india_b.loc[len(region_india_b.index)] = ['North_East',NorthEastMostCommon_b[0][0],NorthEastMostCommon_b[1][0],NorthEastMostCommon_b[2][0]]


# # Save output file

# In[29]:


# Save output File
region_india_a.to_csv("Data/output/region_india_a.csv",index=False)
region_india_b.to_csv("Data/output/region_india_b.csv",index=False)


# In[30]:


region_india_a


# In[31]:


region_india_b


# In[17]:


region_india_b


# In[ ]:




