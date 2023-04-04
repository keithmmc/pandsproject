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


#returning some information about the dimensions of the dataset 
print(f"The iris DataFrame has {iris.ndim} dimensions.\n")
#returning information about the rows and columns of the dataset
print(f"The Iris data set consists of {iris.shape[0]} rows and {iris.shape[1]} columns corresponding to the rows and columns of the csv file.\n")
#returning the number of elements in the dataset
print(f"The iris DataFrame has {iris.size} elements in total.\n")
#returning the index if the dataset
print(f" The index of the DataFrame is: ", iris.index)
    # The DataFrame has both a row and a column index which were automatically assigned when the DataFrame was created.
    # Get the column labels of the iris DataFrame using  'pandas.DataFrame.columns'
print(f"The column labels of the iris DataFrame are: \n", *iris.columns, sep = "   ")
#returning the first ten rows of data to ensure that the file has loaded correctly
print(iris.head(10))
#returning the last ten rows of data to ensure that the file has loaded correctly
print(iris.tail(10))


###going to print the above information to a data file
original_stdout = sys.stdout 

#open the file iris.txt and begin to print the info
with open("iris.txt", "a") as f:
    sys.stdout = f 
    print('\n************************ ANALYSIS OF THE IRIS DATASET *************************\n\n') 
    print('\n************************ basic information on the dataset*********************/n/n')   
    ##outputting the first ten rows of data followed by the last ten rows of data with a random sample
    print(iris.head(10))
    print(iris.tail(10))
    print (iris.sample(5))
    
    print("\n**************************summery of the dataset**********************************/n/n")
    ##Using the `unique()` method on the 'Class' column to show how many different class or species of Iris flower is in the data set
    iris['Class'].unique()
    species_type =iris['Class'].unique()
    print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")
    #getting the summery statistics of the dataset 
    print(iris.describe())
    print("\n*************************The number of null or missing values in the iris dataframe for each column**********\n ")
    print(iris.isnull().sum())
    
    print('\n============================= Median of Attributes ===========================\n') 
    # Print the median of each of the attributes in tabular form
    print(iris.median()) 
    print('\n******************************Mean of Attributes******************************/n')
    print(iris.mean())
    
    sys.stdout = original_stdout
    
   
    