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
print(f" The index of the DataFrame is: ", iris.index)
print("The index for the rows are ",*iris.index)
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
    print("the columns for this dataset are as follows")
    print(iris.columns)
    print("printing the first 10 rows of data of the dataset")
    print(iris.head(10))
    print("printing the final 10 rows of the dataset")
    print(iris.tail(10))
    print (iris.sample(5))
    print (iris[20:30])
    print("\n**************************summery of the dataset**********************************/n/n")
    ##Using the `unique()` method on the 'Class' column to show how many different class or species of Iris flower is in the data set
    iris['Class'].unique()
    species_type =iris['Class'].unique()
    print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")
    iris["Class"].value_counts()
    #getting the summery statistics of the dataset 
    print(iris.describe())
    print("\n*************************The number of null or missing values in the iris dataframe for each column**********\n ")
    print(iris.isnull().sum())
    print ('\n=============================== Duplicate Entries ==============================\n')
    print (iris[iris.duplicated()])
    print('\n============================= Median of Attributes ===========================\n') 
    # Print the median of each of the attributes in tabular form
    print(iris.median()) 
    print('\n******************************Mean of Attributes******************************/n')
    print(iris.mean())
    print('\n******************************Max of Attributes******************************/n')
    print(iris.max())
    

    
sys.stdout = original_stdout
    
    # VISUALISATIONS OF THE IRIS DATA SET

# pandas DataFrame.hist() plots the histograms of the columns on multiple subplots:


iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.suptitle("Histogram of the Iris petal and sepal measurements")
##plt.show()
plt.savefig("histogram")

iris.plot(kind="scatter" , x="sepal_Length" , y="sepal_Width" , color="green" , s=70)
##plt.show()
plt.savefig('scatter1')


iris.plot(kind="scatter" , x="Petal_Length" , y="Petal_Width" , color="red" , s=70)
##plt.show()
plt.savefig('plot2')

print("Boxplots of the distribution of the iris data.")
iris.plot.box(figsize=(6,4))
plt.suptitle("Boxplots of the Iris petal and sepal measurements")
plt.show()
plt.savefig('boxplots')


print("Using pands groupby function to split the iris dataframe by Class of iris species \n")
# Using groupby functions to look at statistics at the class / species level
iris_grouped = iris.groupby("Class")

# Compute count of group, excluding missing values.
iris.groupby("Class").count()
print("The number of observations for each variable for each Iris species in the data set are as follows: \n \n",iris.groupby("Class").count())


plt.title('Class Count')
sns.countplot(data=iris)
plt.savefig('Class_count')
plt.close()

# histogram - general by attribute
fig, axs = plt.subplots(2, 2, figsize=(16, 9))
sns.histplot(data=iris,  color="dodgerblue", ax=axs[0, 0], bins=7)
sns.histplot(data=iris,  color="mediumorchid", ax=axs[0, 1], bins=5)
sns.histplot(data=iris,  color="slateblue", ax=axs[1, 0], bins=7)
sns.histplot(data=iris,  color="teal", ax=axs[1, 1], bins=5)
plt.suptitle('Attributes - General')
plt.savefig('attributes_general')
plt.close()

# Heatmap of correlations between attributes
plt.figure(figsize=(8,8))
sns.heatmap(iris.corr(), annot=True, cmap='Blues')
plt.title('Correlation Between Attributes')
plt.savefig('heatmap')
plt.close()

# defining function for histograms - attributes by species
def histogram_plot(p1, p2, p3):
    
    sns.histplot(data = iris_virginica[p1], color = 'dodgerblue') 
    sns.histplot(data = iris_versicolor[p1], color = 'mediumorchid')
    sns.histplot(data = iris_setosa[p1], color = 'teal')
    plt.xlabel(p2)
    plt.ylabel('Count')
    plt.title('Histogram of ' + p2 + ' by Class') 
    plt.legend(['Iris-virginica', 'Iris-versicolor', 'Iris_setosa'])
    plt.savefig(p3)
    plt.close()





