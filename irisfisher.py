#importing the modlues to begin the project

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import sys


cols = ['sepal_Length', 'sepal_Width','Petal_Length','Petal_Width','Class']
csv = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#reading the CSV file 
iris =  pd.read_csv(csv, names = cols)
#returning the first ten rows of data to ensure that the file has loaded correctly
print(iris.head(10))
print(iris.tail(10)) 


#now that i have return both rows to ensure the file was loaded correctly. I want to test the datatype
print("the columns in this dataframe are as follows n: ")
print(iris.dtypes)

 

###going to print the above information to a data file
original_stdout = sys.stdout 

##open the file iris.txt and begin to print the info
with open("iris.txt", "a") as f:
    sys.stdout = f 
    
    print('\n************************ ANALYSIS OF THE IRIS DATASET *************************\n\n') 
    print(iris.head(10))
    print(iris.tail(10))
    print(iris.dtypes)
    
    print('\n=================== Unique Species Names and Dataset Balance  ==================\n')
    
    