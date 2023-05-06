# pandsproject


this is the project for the pands module in ATU. 



in this project we will be researching the iris data set. this data set was introduced in 1936 by R.A. Fisher A British statistician and biologist in his paper "The use of multiple measurements in taxonomic problems". this data set is available from The UCI Machine Learning Repository. The UCI Machine Learning Repository states "the Iris dataset is widely used in pattern recognition learning. One class is linearly separable from the other two classes, which are not linearly separable from each other. The predicted attribute of the data set is the class of Iris plant to which each observation belongs".

this dataset is a multivariate dataset and consists of 150 instances that has five attributes, four of these attributes are related to the measurements of sepal and of petals, it includes 50 plants each of three classes of Iris plant, where each class is a different type or species of Iris plant. The three classes in the data set are the Iris Setosa, the Iris Versicolor and the Iris Virginica.



http://archive.ics.uci.edu/ml/datasets/Iris

This data set through the years has become one of the main datasets used for learning machine learning, 



Dataset Description
The information that is included in the dataset is as follows:

Sepal length in cm
Sepal width in cm
Petal length in cm
Petal width in cm
Class:
Iris Setosa
Iris Versicolour
Iris Virginica

# <h1> downloading the dataset </h1> #
I downloaded the the data set for for investagting. The Iris Data Set is available from the UC Irvine Machine Learning Repository at http://archive.ics.uci.edu/ml/datasets/Iris in csv. 

I used the following code to achieve this. 

      csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
      # using the attribute information as the column names
      col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
      iris =  pd.read_csv(csv_url, names = col_names)

# <h1> the modules used are as followed  used will be as followed <h1> #

matplotlib
seaborn
pandas 
numpy 

# <h1> investagating the dataset  <h1> #
once I had the CSV file downloaded, I ran some commands using Panda library this has many functions that can be used to explore the Iris data set. Having imported the iris data set from a csv file into a pandas, to help return data this would show that I had downloaded the csv file correctly. This would also help give am overview of the Fisher Iris data set including some summary statistics that describe the data at a high level. 

The first command I ran was the Ndim command to return the axis and the array dimisions of the dataset. Once I ran this command to return the axis dimensions of the object- the number of rows and columns in the table of data. this command also returned the number of rows that has observations and rows that contains variables in this data set. 

The next command I ran was the index command this command shows the index that was assigned when the dataframe was created when reading the csv file. 

After I had got the index of the dataframe I then looked at the size of each element in the dataframe. 

I followed of the index and size commands with the column  to show all the column labels in the dataset. 

After I had the column information, I used the axes command to get a list representing the axes of the DataFrame and will show the row axis labels first and then the column axis labels. This essentially shows same information as the index and columns attributes. I then followed this up with dtypes command to show all the datatypes of the dataframe. 

I then wanted to gather information on the first ten rows and last ten rows of rows in the dataframe. to this i used the head and tail commands. 


I used these commands as follows 


print(f"The iris DataFrame has {iris.ndim} dimensions.\n")

print(f"The Iris data set consists of {iris.shape[0]} rows and {iris.shape[1]} columns corresponding to the rows and columns of the csv file.\n")

print(f"The iris DataFrame has {iris.size} elements in total.\n")

print(f" The index of the DataFrame is: ", iris.index)

print(f" The index of the DataFrame is: ", iris.index)
print("The index for the rows are ",*iris.index)
print(f"The column labels of the iris DataFrame are: \n", *iris.columns, sep = "   ")

print(iris.head(10))

print(iris.tail(10))


<p>

after I had this information I wanted to get subsets of the iris data for each class in the dataframe. To acheive this I used the groupby command, this spilt the data into groups and then returns the information. 

I used the following code to do this 

print("Using pands groupby function to split the iris dataframe by Class of iris species \n")

iris_grouped = iris.groupby("Class")

print(iris.groupby("Class").describe().T)
print("summary statistics for each Class of Iris in the data set \n")


iris.groupby("Class").count()
print("The number of observations for each variable for each Iris species in the data set are as follows: \n \n",iris.groupby("Class").count())


print("The mean or average measurement for each group of Iris Species in the dataset is \n\n",iris.groupby('Class').mean())
iris.groupby('Class').mean()

iris.groupby("Class").first()
print("The first observation in each Class of Iris plant in the Iris dataset are: \n  \n",iris.groupby("Class").first())

print("The last observation in each Class of Iris plant in the Iris dataset are: \n  \n",iris.groupby("Class").last())
iris.groupby("Class").last()


iris.groupby("Class").head(3)
print("The first three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").head(3))


iris.groupby("Class").tail(3)
print("The last three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").tail(3))

iris.groupby("Class").max()
print("The maximum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").max())

iris.groupby("Class").min()
print("The minimum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").min())



iris_ranges = iris_grouped.max() - iris_grouped.min()
print("The range of the values in the dataset are as follows: \n",iris_ranges)

iris.groupby("Class").mean()

iris.groupby("Class").median()

print(iris_grouped.count())

print(iris_grouped.mean())

means = iris.groupby("Class").mean().T

# <h1> the next step was to output infomration to a text file <h1> # 
After I had done some investagating into the dataframe, I wanted to save some of this information into a text file. To this I imported the sys module and opened the file in append mode. 

the first piece of information I wanted to output was information on the columns with the first ten and last rows I combined this with the sample command to get five random rows of information returned. I then spliced the dataframe to return the information from row 20 to 30. 

I used the following code to do this 

print("the columns for this dataset are as follows")
    print(iris.columns)
    print("printing the first 10 rows of data of the dataset")
    print(iris.head(10))
    print("printing the final 10 rows of the dataset")
    print(iris.tail(10))
    print (iris.sample(5))
    print (iris[20:30])

Once I had got this information I then wanted to output the size of each class and the amount of columns in each class. 

I used the following code to do this 
 iris['Class'].unique()
    species_type =iris['Class'].unique()
    print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")
    iris["Class"].value_counts()

