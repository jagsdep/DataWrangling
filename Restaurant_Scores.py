# The Health Department has developed an inspection report and scoring system. After conducting an inspection of the facility, the Health Inspector calculates a score based on the violations observed. Violations can fall into:high risk category: records specific violations that directly relate to the transmission of food borne illnesses, the adulteration of food products and the contamination of food-contact surfaces.moderate risk category: records specific violations that are of a moderate risk to the public health and safety.low risk category: records violations that are low risk or have no immediate risk to the public health and safety.The score card that will be issued by the inspector is maintained at the food establishment and is available to the public in this dataset.


from pandas.core.indexes.base import InvalidIndexError
import numpy as np
import pandas as pd 
print(pd.__version__)
#import matplotlib.pyplot as plt


df = pd.read_csv('restaurant_scores.csv') #we reading the data from .csv file and stored in dataframe df

print(df.shape) # displays rows and columns

print(df.info())
print(df.head()) #by default shows the tope 5 rows but we can add the number of rows
print(df.head(5))
print(df.tail()) #checks last few rows

print(df.describe()) #it gives statistical data like count, mean, std, min
print(df.mean())
print(df['Analysis Neighborhoods'].mean())
print(df['Analysis Neighborhoods'].min())
print(df['Analysis Neighborhoods'].plot())

print(df['business_name'])

def sort_values():
    df = pd.read_csv('restaurant_scores.csv', nrows=20) 
    print(df['business_name'])
    df =  df.sort_values('business_name', ascending = True)
    print(df)
    print(df['business_name'])
sort_values()

def subset_values():
    df = pd.read_csv('restaurant_scores.csv', nrows=5) 
    df_sub=df.sort_values('business_name', ascending = True)
    print(df_sub)
    
subset_values()

scores = pd.read_csv('restaurant_scores.csv') 
print(scores.isnull()) #this will return true wherever there is null value in the database
print(scores.isnull().sum()) #gives the total sum of null values for each column 
print(scores.isnull().sum().sum()) #Total null values in dataset

#task is to replace the null value with 0
scores = scores.replace(to_replace=np.nan, value=0) #to_replace is what we want to replace so that is null value and since numpy contains an object for null value and value is the value that need to be in place of replace
print(scores)

#Identify the outliers 

df = pd.read_csv('restaurant_scores.csv') 

# Transforming one column to many 
scores = pd.read_csv('restaurant_scores.csv', nrows=5) 

a = scores.pivot("business_name", "risk_category", "inspection_score")
print(a)







     













