#!/usr/bin/env python
# coding: utf-8

# # **Problem 2**
# ---

# In[1]:


import pandas as pd

cars = pd.read_csv('cars.csv')
cars


# > (a) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars

# In[5]:


odd = cars.iloc[:,::2]      #I use .iloc[] to only input only the odd number colums
odd_clms = odd.head()       #This is for the first 5 rows
odd
odd_clms


# > (b) Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[6]:


cars.loc[cars['Model'] == 'Mazda RX4']     #This is to locate the model iof Mazda RX4


# > (c) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[26]:


cmro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]   #It will select on what column cyl of the Camaro Z28
print ("The number of cylinders of the Camaro Z28:", cmro_cyl)


# > (d) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[25]:


Mzda = cars.loc[cars["Model"]== 'Mazda RX4 Wag', ['Model','cyl', 'gear']]    ##This is to locate the model, cyl, and gear of each car
Frd = cars.loc[cars["Model"]== 'Ford Pantera L', ['Model','cyl', 'gear']]
Hnda = cars.loc[cars["Model"]== 'Honda Civic', ['Model','cyl', 'gear']]

print("The number of gears and cylinders of the presented cars are: ")
pd.concat([Mzda, Frd, Hnda])                                                       

