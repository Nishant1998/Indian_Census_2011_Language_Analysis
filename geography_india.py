#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import scipy.stats as stats


# ## Reading Data
# ### Reading census data

# In[3]:


censusData = pd.read_csv("Data/CensusData.csv",low_memory=False,index_col=False)
censusData.head(5)


# ### Reading c18 Data

# In[10]:


c18 = pd.read_csv("Data/c18_modified.csv",index_col=False)
c18.head()


# In[11]:


def calculate_p_values(a,b):
    _,p_value=stats.ttest_ind(a,b,equal_var=False)
    return p_value


# In[12]:


# find male to female ratio

population_rural = censusData[(censusData['TRU']== 'Rural') & (censusData['Level']== 'India')].TOT_P.to_list()
population_urban = censusData[(censusData['TRU']== 'Urban') & (censusData['Level']== 'India')].TOT_P.to_list()

censusRural = censusData[(censusData['TRU']== 'Rural') & (censusData['Level']== 'STATE')]
censusUrban = censusData[(censusData['TRU']== 'Urban') & (censusData['Level']== 'STATE')]

population_rural.extend(censusRural.TOT_P.to_list())
population_urban.extend(censusUrban.TOT_P.to_list())

population_rural = np.array(population_rural)
population_urban = np.array(population_urban)
urbanToRuralRatio = population_urban / population_rural


# In[13]:


# find language ratio for male and female
c18_Urban = c18[(c18['Age_group']=='Total') & (c18['TRU']=='Urban')]
c18_Rural = c18[(c18['Age_group']=='Total') & (c18['TRU']=='Rural')]


urban_3 = np.array(c18_Urban.Persons_3.to_list())
rural_3 = np.array(c18_Rural.Persons_3.to_list())
urban_2 = np.array(c18_Urban.Persons_2.to_list()) - np.array(c18_Urban.Persons_3.to_list())
rural_2 = np.array(c18_Rural.Persons_2.to_list()) - np.array(c18_Rural.Persons_3.to_list())
urban_1 = population_urban - np.array(c18_Urban.Persons_2.to_list())
rural_1 = population_rural - np.array(c18_Rural.Persons_2.to_list())

ratio_1 = urban_1 / rural_1
ratio_2 = urban_2 / rural_2
ratio_3 = urban_3 / rural_3


# In[14]:


# calculate p value
p_value_1 = calculate_p_values(ratio_1,urbanToRuralRatio)
p_value_2 = calculate_p_values(ratio_2,urbanToRuralRatio)
p_value_3 = calculate_p_values(ratio_3,urbanToRuralRatio)


# In[15]:


''' WHAT IS MALE AND FEMALE PERCENTAGE? ADD THAT '''
data_1 = {'State_Code': range(36),'urban_percentage': urban_1/population_urban*100,'rural_percentage':rural_1/population_rural*100, 'p_value':p_value_1}
data_2 = {'State_Code': range(36),'urban_percentage': urban_2/population_urban*100,'rural_percentage':rural_2/population_rural*100, 'p_value':p_value_2}
data_3 = {'State_Code': range(36),'urban_percentage': urban_3/population_urban*100,'rural_percentage':rural_3/population_rural*100, 'p_value':p_value_3}


# In[16]:


# make dataframe
geography_india_a = pd.DataFrame(data_1)
geography_india_b = pd.DataFrame(data_2)
geography_india_c = pd.DataFrame(data_3)

# Save output File
geography_india_a.to_csv("Data/output/geography_india_a.csv",index=False)
geography_india_b.to_csv("Data/output/geography_india_b.csv",index=False)
geography_india_c.to_csv("Data/output/geography_india_c.csv",index=False)

