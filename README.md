# **Programming Assignment 3**
---
## **PHYTON DATA ANALYSIS (PANDAS)**

References:
* Link: [Problem 1 ipnyb file](https://github.com/ajtdengust326/DUADICO_2ECE-B_ECE2112_Programming-Assignment-3/edit/main/README.md)
* Link: [Problem 1 py file](https://github.com/ajtdengust326/DUADICO_2ECE-B_ECE2112_Programming-Assignment-3/edit/main/README.md)
* Link: [Problem 2 ipnyb file](https://github.com/ajtdengust326/DUADICO_2ECE-B_ECE2112_Programming-Assignment-3/edit/main/README.md)
* Link: [Problem 2 py file](https://github.com/ajtdengust326/DUADICO_2ECE-B_ECE2112_Programming-Assignment-3/edit/main/README.md)
_____________

### **PROBLEM 1**
> (a) Load the corresponding .csv file into a data frame named cars using pandas
> 
We're using pandas, so we must import the library of pandas 
```phyton
import pandas as pd                               
```
To output the download *.csv* file I used the *.raed_csv('')* as what I've learned
```phyton
cars = pd.read_csv('cars.csv')                              
```
Don't use print() because it will not output as it inteded
```phyton
cars                             
```
> (b) Display the first five and last five rows of the resulting cars.
> 
To combine and display the first and last 5 rows, .concat() is used to combine them
```
print("The first and last five rows:")
display = pd.concat([cars.iloc[0:5],cars.iloc[27:32]])  
display
```
This is to save the .ipnyb file in to .py 
```
get_ipython().system('jupyter nbconvert --to script "Duadico_Pandas-P1 .ipynb"')
```
_____________
### **PROBLEM 2**
Used the code again in [Problem 1](https://github.com/ajtdengust326/DUADICO_2ECE-B_ECE2112_Programming-Assignment-3/edit/main/README.md) to display the .csv file
```
import pandas as pd

cars = pd.read_csv('cars.csv')
cars
```
> (a) Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars

I use .iloc[] to only input only the odd number colums
```
odd = cars.iloc[:,::2]   
```
This is for the first 5 rows
```
odd_clms = odd.head()
odd   
odd_clms
```
> (b) Display the row that contains the ‘Model’ of ‘Mazda RX4’.

This is to locate the model iof Mazda RX4
```
cars.loc[cars['Model'] == 'Mazda RX4']
```
> (c) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

It will select on what column cyl of the Camaro Z28
```
cmro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print ("The number of cylinders of the Camaro Z28:", cmro_cyl)
```
> (d) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

This is to locate the model, cyl, and gear of each car
```
Mzda = cars.loc[cars["Model"]== 'Mazda RX4 Wag', ['Model','cyl', 'gear']]    ##This is to locate the model, cyl, and gear of each car
Frd = cars.loc[cars["Model"]== 'Ford Pantera L', ['Model','cyl', 'gear']]
Hnda = cars.loc[cars["Model"]== 'Honda Civic', ['Model','cyl', 'gear']]

print("The number of gears and cylinders of the presented cars are: ")
pd.concat([Mzda, Frd, Hnda])                                                       
```
To save the .ipnyb file into .py file
```
!jupyter nbconvert --to script "Duadico_Pandas-P2 .ipynb"
```

