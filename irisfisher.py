#importing the modlues to begin the project

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import sys

#setting up the csv file for reading I am breaking this down into columns this will be read by pandas 

cols = ['sepal_Length', 'sepal_Width','Petal_Length','Petal_Width','Class']
csv = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#reading the CSV file 
iris =  pd.read_csv(csv, names = cols)


# using the ndim command to return some information about the dimensions of the dataset 
print(f"The iris DataFrame has {iris.ndim} dimensions.\n")
#using the shape command to return some information about the rows and columns of the dataset
print(f"The Iris data set consists of {iris.shape[0]} rows and {iris.shape[1]} columns corresponding to the rows and columns of the csv file.\n")
#using the size command to return the number of elements in the dataset
print(f"The iris DataFrame has {iris.size} elements in total.\n")
#returning the index if the dataset
print(f" The index of the DataFrame is: ", iris.index)
    # The DataFrame has both a row and a column index which were automatically assigned when the DataFrame was created.
    # Get the column labels of the iris DataFrame using  'pandas.DataFrame.columns'
print(f" The index of the DataFrame is: ", iris.index)
print("The index for the rows are ",*iris.index)
print(f"The column labels of the iris DataFrame are: \n", *iris.columns, sep = "   ")
#returning the first ten rows of the dataset
print(iris.head(10))
#returning the last ten rows of the dataset
print(iris.tail(10))



# GROUP BY 

print("Using pands groupby function to split the iris dataframe by Class of iris species \n")
# Using groupby command to look at statistics at the class / species level
iris_grouped = iris.groupby("Class")
#describing the class using the groupby command again 
print(iris.groupby("Class").describe().T)
print("summary statistics for each Class of Iris in the data set \n")

# Compute count of group, excluding missing values.
iris.groupby("Class").count()
print("The number of observations for each variable for each Iris species in the data set are as follows: \n \n",iris.groupby("Class").count())

# Groupby Class of Iris plant and return the mean of the remaining columns in each group.

print("The mean or average measurement for each group of Iris Species in the dataset is \n\n",iris.groupby('Class').mean())
iris.groupby('Class').mean()
# Group by Class of Iris plant and then return the first observations in each group
iris.groupby("Class").first()
print("The first observation in each Class of Iris plant in the Iris dataset are: \n  \n",iris.groupby("Class").first())

# Group by Class of Iris and then return the last observations in each group
print("The last observation in each Class of Iris plant in the Iris dataset are: \n  \n",iris.groupby("Class").last())
iris.groupby("Class").last()

# get the first 3 rows in each group 
iris.groupby("Class").head(3)
print("The first three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").head(3))

# get the last 3 rows in each group
iris.groupby("Class").tail(3)
print("The last three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").tail(3))

# get max of group values
iris.groupby("Class").max()
print("The maximum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").max())

# get min of group values
iris.groupby("Class").min()
print("The minimum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").min())

# There does not seem to be a range function to see the range of values so I am going to calculate these ranges here.
# by taking the differences between the mimimum and the maximum values

iris_ranges = iris_grouped.max() - iris_grouped.min()
print("The range of the values in the dataset are as follows: \n",iris_ranges)

###going to print the above information to a data file
original_stdout = sys.stdout 

#open the file iris.txt and begin to print the info
with open("iris.txt", "a") as f:
    sys.stdout = f 
    print('\n************************ ANALYSIS OF THE IRIS DATASET *************************\n\n') 
    print('\n************************ basic information on the dataset*********************/n/n')   
    ##outputting the first ten rows of data followed by the last ten rows of data with a random sample and I am also returning the column information also using the splice function to return information on columns 20-30 
    print("the columns for this dataset are as follows")
    print(iris.columns)
    print("printing the first 10 rows of data of the dataset")
    print(iris.head(10))
    print("printing the final 10 rows of the dataset")
    print(iris.tail(10))
    print (iris.sample(5))
    print (iris[20:30])
    print("\n**************************summery of the dataset**********************************/n/n")
    ##Using the `unique()` method on the 'Class' column to show how many different class is in the data set
    iris['Class'].unique()
    species_type =iris['Class'].unique()
    print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")
    #getting the value of each class
    iris["Class"].value_counts()
    #getting the summery statistics of the dataset 
    print(iris.describe())
    print("\n*************************The number of null or missing values in the iris dataframe for each column**********\n ")
    #returning the number of columns that are null
    print(iris.isnull().sum())
    print ('\n=============================== Duplicate Entries ==============================\n')
    #returning the number of duplicate attributes in the dataset
    print (iris[iris.duplicated()])
    print('\n============================= Median of Attributes ===========================\n') 
    #returning the median of each of the attributes in tabular form
    print(iris.median()) 
    print('\n******************************Mean of Attributes******************************/n')
   #returning the mean of the attributes in tabular form
    print(iris.mean())
    print('\n******************************Max of Attributes******************************/n')
#returning the max of the attributes in tabular form
    print(iris.max())
    

#closing of the text file  
sys.stdout = original_stdout
    
# VISUALISATIONS OF THE IRIS DATA SET
# using the pandas DataFrame.hist() to plot the histograms of the columns on multiple subplots this will show the petal and sepal measurements 
iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.suptitle("Histogram of the Iris petal and sepal measurements")
plt.show()


#using seabourn to return the count of each class 
sns.set(style="ticks", palette="pastel")
plt.title('Class Count')
sns.countplot(iris['Class'])


# plotting 4 plots on a 2 by 2 grid, do not want to share the y axis between plots. Setting the figure size 
f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
# passing a panda Series as the x and y parameters to the boxplot. 
# Using the Class column (categorical) and one of the sepal or petal measurements (numerical) for each subplot

# setting the hue = Class so that the points will be coloured on the plot according to their Class/species type.
sns.boxplot(x="Class", y="sepal_Length", data=iris, ax=axes[0,1])
sns.boxplot(x="Class", y="sepal_Width", data=iris, ax=axes[1,1])
sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])

sns.boxplot(x="Class", y="Petal_Width",hue = "Class",data=iris, ax=axes[1,0])

# adding a title to the plot
f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")

#using a pairplot to get the relationship of the attributes 
sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
sns.pairplot(iris, hue='Class', palette="crest")
plt.show()


# Heatmap of correlations between attributes
plt.figure(figsize=(8,8))
sns.heatmap(iris.corr(), annot=True, cmap='Blues')
plt.title('Correlation Between Attributes')
plt.show()

#using a violingplot to return the length and width of each class
fig, axes = plt.subplots(2, 2, figsize=(16,10))
sns.violinplot( y='Petal_Width', x= 'Class', data=iris,  ax=axes[0, 0])
sns.violinplot( y='Petal_Length', x= 'Class', data=iris, ax=axes[0, 1])
sns.violinplot( y='sepal_Length', x= 'Class', data=iris,  ax=axes[1, 0])
sns.violinplot( y='sepal_Width', x= 'Class', data=iris, ax=axes[1, 1])
plt.show()



sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "sepal_Width") \
.add_legend()

sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "sepal_Length") \
.add_legend()

sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "Petal_Length") \
.add_legend()

sns.FacetGrid(iris, hue="Class", height=5) \
.map(sns.distplot, "Petal_Width") \
.add_legend()
plt.show()

iris = sns.load_dataset('iris')
sns.lmplot( x="petal_length" , y="petal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()


iris = sns.load_dataset('iris')
sns.lmplot( x="sepal_length" , y="sepal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()

