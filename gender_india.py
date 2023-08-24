#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy.stats as stats


# ## Reading Data
# ### Reading census data

# In[2]:


censusData = pd.read_csv("Data/CensusData.csv",low_memory=False,index_col=False)
censusData.head(5)


# ### Reading c18 Data

# In[3]:


c18 = pd.read_csv("Data/c18_modified.csv",index_col=False)
c18.head(5)


# In[4]:


def calculate_p_values(a,b):
    _,p_value=stats.ttest_ind(a,b,equal_var=False)
    return p_value


# In[ ]:





# In[8]:


# find male to female ratio
indPop = censusData[(censusData['TRU']== 'Total') & (censusData['Level']== 'India')]
population_male = indPop.TOT_M.to_list()
population_female = indPop.TOT_F.to_list()

censusState = censusData[(censusData['TRU']== 'Total') & (censusData['Level']== 'STATE')]

population_male.extend(censusState.TOT_M.to_list())
population_female.extend(censusState.TOT_F.to_list())
population_male = np.array(population_male)
population_female = np.array(population_female)
maleToFemaleRatio = population_male / population_female


# In[9]:


# find language ratio for male and female
c18Total = c18[(c18['Age_group']=='Total') & (c18['TRU']=='Total')]
male_3 = np.array(c18Total.Males_3.to_list())
female_3 = np.array(c18Total.Females_3.to_list())
male_2 = np.array(c18Total.Males_2.to_list()) - np.array(c18Total.Males_3.to_list())
female_2 = np.array(c18Total.Females_2.to_list()) - np.array(c18Total.Females_3.to_list())
male_1 = population_male - np.array(c18Total.Males_2.to_list())
female_1 = population_female - np.array(c18Total.Females_2.to_list())

ratio_1 = male_1 / female_1
ratio_2 = male_2 / female_2
ratio_3 = male_3 / female_3


# In[13]:


# find p value
## for one language
p_value_1 = calculate_p_values(ratio_1,maleToFemaleRatio)
p_value_2 = calculate_p_values(ratio_2,maleToFemaleRatio)
p_value_3 = calculate_p_values(ratio_3,maleToFemaleRatio)


# In[14]:


# add data in dictionary
data_1 = {'State_Code': range(36),'male_percentage': male_1/population_male*100,' female_percentage':female_1/population_female*100, 'p_value':p_value_1}
data_2 = {'State_Code': range(36),'male_percentage': male_2/population_male*100,' female_percentage':female_2/population_female*100, 'p_value':p_value_2}
data_3 = {'State_Code': range(36),'male_percentage': male_3/population_male*100,' female_percentage':female_3/population_female*100, 'p_value':p_value_3}


# In[17]:


# make dataframe
gender_india_a = pd.DataFrame(data_1)
gender_india_b = pd.DataFrame(data_2)
gender_india_c = pd.DataFrame(data_3)

# Save output File
gender_india_a.to_csv("Data/output/gender_india_a.csv",index=False)
gender_india_b.to_csv("Data/output/gender_india_b.csv",index=False)
gender_india_c.to_csv("Data/output/gender_india_c.csv",index=False)


# In[ ]:





# In[ ]:




