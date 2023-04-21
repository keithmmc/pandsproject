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

sns.set(style="ticks", palette="pastel")

# plotting 4 plots on a 2 by 2 grid, do not want to share the y axis between plots. Setting the figure size 
f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
# pass a panda Series as the x and y parameters to the boxplot. 
# Using the Class column (categorical) and one of the sepal or petal measurements (numerical) for each subplot

# setting the hue = Class so that the points will be coloured on the plot according to their Class/species type.
sns.boxplot(x="Class", y="sepal_Length", data=iris, ax=axes[0,1])
sns.boxplot(x="Class", y="sepal_Width", data=iris, ax=axes[1,1])
sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])

sns.boxplot(x="Class", y="Petal_Width",hue = "Class",data=iris, ax=axes[1,0])

# adding a title to the plot
f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")

sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
sns.pairplot(iris, hue='Class', palette="crest")
plt.show()


print("Using pands groupby function to split the iris dataframe by Class of iris species \n")
# Using groupby functions to look at statistics at the class / species level
iris_grouped = iris.groupby("Class")

# Compute count of group, excluding missing values.
iris.groupby("Class").count()
print("The number of observations for each variable for each Iris species in the data set are as follows: \n \n",iris.groupby("Class").count())


# Heatmap of correlations between attributes
plt.figure(figsize=(8,8))
sns.heatmap(iris.corr(), annot=True, cmap='Blues')
plt.title('Correlation Between Attributes')
plt.savefig('heatmap')
plt.close()


# trying to graph histograms with Probability Density Function 
sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "sepal_Length") \
.add_legend()

sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "sepal_Width") \
.add_legend()

sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "Petal_Length") \
.add_legend()

sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "Petal_Width") \
.add_legend()
plt.show()

