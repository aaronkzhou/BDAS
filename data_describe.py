# importing pandas module  
import pandas as pd  
  
# importing regex module 
import re 
    
# making data frame  
data = pd.read_csv("./gender.csv")  
    
# removing null values to avoid errors  
data.dropna(inplace = True)  
  
# percentile list 
perc =[.20, .40, .60, .80] 
  
# list of dtypes to include 
include =['object', 'float', 'int']
  
# calling describe method 
desc = data.describe(percentiles = perc, include = include) 
  
# display 
print(desc) 