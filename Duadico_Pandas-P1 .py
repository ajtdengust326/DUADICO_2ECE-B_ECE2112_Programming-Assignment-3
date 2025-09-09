#!/usr/bin/env python
# coding: utf-8

# # **Problem 1**
# ---

# 
# > (a) Load the corresponding .csv file into a data frame named cars using pandas

# In[33]:


import pandas as pd               #We're using pandas so we must impot the library of pandas 

cars = pd.read_csv('cars.csv')    #To output the download .csv file I used the .raed_csv('') as what i've learned
cars                              #Don't use print() because it will not output as in inteded


# > (b) Display the first five and last five rows of the resulting cars.

# In[34]:


print("The first and last five rows:")
display = pd.concat([cars.iloc[0:5],cars.iloc[27:32]])  #To combine and display the first and last 5 rows, 
display


# In[39]:


get_ipython().system('jupyter nbconvert --to script "Duadico_Pandas-P1 .ipynb"')


# In[ ]:




