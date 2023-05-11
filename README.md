# pandsproject



# <h1> Python and other software tools used in this project <h1>
this is the project for the pands module in ATU. 

Python and other software tools used in this project
The purpose of this project is to investigate the Fisher Iris data set described above using Python code. Python is a high level interpreted general purpose programming language. The Python interpreter and its extensive standard library are freely available to all. Along with the Python standard library, there are many libraries that enhance the usage of Python and make it a powerful tool for performing data analytics and machine learning.

The free and open source Visual Studio code editor was used to write the Python code and the Markdown content. Visual Studio Code can be downloaded here.

How to download this repository
Go to the URL for the repository on GitHub at https://github.com/keithmmc/pandsproject.git
Click the green Clone or download button
Python 3
To be able to run this script, you need to have Python 3 installed. You can check this on the command line using python -V. If you do not have Python 3 installed go to https://www.python.org/downloads/ and follow the instructions there.

Python comes with a library of standard modules that can perform a wide range of tasks. These modules can be imported using the import function. In addition to the standard modules, there are many third-party packages which enhance it's functionality and I use some of these packages in this project outlined below, in particular the pandas package which provides data structures and data analysis tools for the Python programming langauge. These packages can be also be imported but they first need to be installed on your system. See Installing Packages of the Python Documentation. pip is the package installer for Python and can be used to install packages from the PyPI repository of software for the Python programming language.

pandas installation instructions recommend installing the package as part of the Anaconda distribution, a cross platform distribution for data analysis and scientific computing using conda install pandas. The seaborn package can be installed using pip install seaborn or conda install seaborn. seaborn installation instructions

The pandas library is the main python library being used in this project. According to the pandas package overview

pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python.

pandas provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. It is designed for working with data that is in a tabular format containing an ordered collection of columns where each column can have a different value type. This makes it ideal for exploring a structured tabular dataset such as Iris which contains several numerical columns and one categorical column.

seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

The seaborn library is used for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. It provides a high-level interface for creating nice looking and informative plots. It has many useful features for examining relationships between multiple variables such as those in the Iris dataset.

matplotlib.org

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms

How to run the Python code
To run the Python script, first navigate to the folder downloaded from this repository.

At the command line enter python <program_name> for example: $ python project_iris.py

The Python program can also be run inside the environment of an iPython session using the %run command. % run project_iris.py
I used ipython to run interactive code. This was very useful in testing sections of the script, rather than running the entire Python script for each change.

There are several plots produced by the script. I have saved these to .png files in the images folder of the repository. The plots can be printed by uncommenting the 'plt.show()` command. Some of these plots are shown in this Readme file below.

The output of the Python script (excluding plot images) can be saved to a text file by appending >'filename.txt'.

Loading Python libraries
The libraries mentioned above must first be imported before they can be used by the script.

The pandas library is imported at the very start of the script using import pandas as pd where pd is a shorter alias name that is used by convention to save having to write pandas each time it is used. Therefore, wherever pd is used in the script, it is referring to the pandas library. Similarly, the seaborn library is imported using the alias sn and thereafter referred to using sn. Once these packages are loaded, all of the available functions can be used by the script.

import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns
Getting help in Python
To get help on any python command, use the python help function as outlined in the Python help command document with the command in parentheses.
For example, help(pd) will show help on the python pandas package while help(pd.DataFrame.describe()) provides help on the describe function of the pandas DataFrame.
The documentation pages for each of the python packages that are used in this project provided details of all the commands for that package. I found these resources quite valuable for this project and referred to them extensively over the course of this project, both when looking for a function to do something in particular but also for getting a start with the packages as the documentation pages are quite comprehensive and outline the different functions of the various packages.

# <h1> the data set <h1> #

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

The iris DataFrame has 2 dimensions.
 
print(f"The Iris data set consists of {iris.shape[0]} rows and {iris.shape[1]} columns corresponding to the rows and columns of the csv file.\n")

The Iris data set consists of 150 rows and 5 columns corresponding to the rows and columns of the csv file.

print(f"The iris DataFrame has {iris.size} elements in total.\n")
The iris DataFrame has 750 elements in total.

print(f" The index of the DataFrame is: ", iris.index)
The index of the DataFrame is:  RangeIndex(start=0, stop=150, step=1)

print("The index for the rows are ",*iris.index)
The index for the rows are  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 
100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149

print(f"The column labels of the iris DataFrame are: \n", *iris.columns, sep = "   ")
The column labels of the iris DataFrame are: 
   sepal_Length   sepal_Width   Petal_Length   Petal_Width   Class

print(iris.head(10))
this


print(iris.tail(10))


 
<p>

after I had this information I wanted to get subsets of the iris data for each class in the dataframe. To acheive this I used the groupby command, this spilt the data into groups and then returns the information. 

I used the following code to do this 
print("Using pands groupby function to split the iris dataframe by Class of iris species \n")

iris_grouped = iris.groupby("Class")

print(iris.groupby("Class").describe().T) 
Using pands groupby function to split the iris dataframe by Class of iris species  




print("summary statistics for each Class of Iris in the data set \n")

iris.groupby("Class").count() print("The number of observations for each variable for each Iris species in the data set are as follows: \n \n",iris.groupby("Class").count())
summary statistics for each Class of Iris in the data set

The number of observations for each variable for each Iris species in the data set 
are as follows:


iris.groupby("Class").first() print("The first observation in each Class of Iris plant in the Iris dataset are: \n \n",iris.groupby("Class").first())



print("The last observation in each Class of Iris plant in the Iris dataset are: \n \n",iris.groupby("Class").last()) iris.groupby("Class").last()



iris.groupby("Class").head(3) print("The first three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").head(3))


iris.groupby("Class").tail(3) print("The last three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").tail(3))



iris.groupby("Class").max() print("The maximum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").max())



iris.groupby("Class").min() print("The minimum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").min())



iris_ranges = iris_grouped.max() - iris_grouped.min() print("The range of the values in the dataset are as follows: \n",iris_ranges)



After I had done some investagating into the dataframe, I wanted to save some of this information into a text file. To this I imported the sys module and opened the file in append mode. 


# <h1> Visualising the Iris data set <h1> # 

In this section I will discuss visulising the dataset, the first plot I created was a histogram, This histogram returned the Petal length petal width sepal length and sepal width, The histogram for the petal lengths show a clear group of observations having petal lengths that are much smaller than the rest of the observations and similarly so with the petal widths. The sepal lengths show quite a bit of variation with a number of peaks while sepal widths seem to be centred around 3 cms but with a few smaller peaks at both sides of 3 cms. To create this hsitogram I used the following the code. 

iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.suptitle("Histogram of the Iris petal and sepal measurements")
plt.show()

# <p> #
The next visualtion I ran was to get the breakdown of each class using seaborn, this should show that there is exactly 50 per count for each class. I used the following code to achieve this 
sns.set(style="ticks", palette="pastel")
plt.title('Class Count')
sns.countplot(iris['Class'])



I then used a boxplot to show various statistics in one go, including the median, quantiles, interquartile range, outliers etc. The length of the box is the interquartile range and measures the variability in the data set. The interquartile range (IQR) is the middle 50% of the data and can show the spread or variation of the data. The whiskers show if the data is skewed in one direction or the other. The median is the line through the box.

Along with showing the distribution of values within each category, boxplots also allow for comparisons across the various classes. The hue is set to 'Class' so that the points will be coloured on the plot according to their Class/species type. I used the following the code to achieve this. 

f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
sns.boxplot(x="Class", y="sepal_Length", data=iris, ax=axes[0,1])
sns.boxplot(x="Class", y="sepal_Width", data=iris, ax=axes[1,1])
sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])
sns.boxplot(x="Class", y="Petal_Width",hue = "Class",data=iris, ax=axes[1,0])
f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")

After I created the boxplots I wanted to get to visualise relationships between each variable and produce a matrix of relationships between each attribute in the dataset. I used pairplots to do this. I used the following code to achieve this 

sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
sns.pairplot(iris, hue='Class', palette="crest")
plt.show()

After this I used a heat map to show the correlations between the four classes in the dataset this heatmap should show that the sepal length and sepal width are slightly corrlated with each other, I used the following code to achieve this 
plt.figure(figsize=(8,8))
sns.heatmap(iris.corr(), annot=True, cmap='Blues')
plt.title('Correlation Between Attributes')
plt.show()

after this I wanted used a violin plot. This will show the density of the length and width in the classes. The thinner part denotes that there is less density whereas the fatter part conveys higher density. The following information can be seen from this,Setosa is having less distribution and density in case of petal length & width
Versicolor is distributed in a average manner and average features in case of petal length & width Virginica is highly distributed with large no .of values and features in case of sepal length & width High density values are depicting the mean/median values, for example: Iris Setosa has highest density at 5.0 cm ( sepal length feature) which is also the median value(5.0) as per the table. I used the following code to achive this. 

fig, axes = plt.subplots(2, 2, figsize=(16,10))
sns.violinplot( y='Petal_Width', x= 'Class', data=iris,  ax=axes[0, 0])
sns.violinplot( y='Petal_Length', x= 'Class', data=iris, ax=axes[0, 1])
sns.violinplot( y='sepal_Length', x= 'Class', data=iris,  ax=axes[1, 0])
sns.violinplot( y='sepal_Width', x= 'Class', data=iris, ax=axes[1, 1])
plt.show()


After I created the violin plots I wanted to return histograms with Probability Density Function. 

I used the following code to achieve this 
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

this will show the following Plot 1 shows that there is a significant amount of overlap between the species on sepal length, so it is not an effective Classification feature
Plot 2 shows that there is even higher overlap between the classes on sepal width, so it is not an effective Classification feature
Plot 3 shows that petal length is a good Classification feature as it clearly separates the species . The overlap is extremely less (between Versicolor and Virginica) , Setosa is well separated from the rest two
Just like Plot 3, Plot 4 also shows that petal width is a good Classification feature . The overlap is significantly less (between Versicolor and Virginica) , Setosa is well separated from the rest two

the last plot I wanted to create was a scatter plot to show the comparsion between the length and width of each class. 

I used the following code to do this 
iris = sns.load_dataset('iris')
sns.lmplot( x="petal_length" , y="petal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()


iris = sns.load_dataset('iris')
sns.lmplot( x="sepal_length" , y="sepal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()




# references # 
https://archive.ics.uci.edu/ml/datasets/iris

https://en.wikipedia.org/wiki/Iris_flower_data_set

https://matplotlib.org/index.html

https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/

https://www.kaggle.com/code/crbelhekar619/iris-dataset-eda-visualization/notebook

https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/run-calculations-summary-statistics-pandas-dataframes/

https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html

https://pandas.pydata.org/docs/user_guide/10min.html

https://seaborn.pydata.org/

https://www.w3schools.com/python/pandas/pandas_analyzing.asp

https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp#

https://realpython.com/python-histograms/

https://python-graph-gallery.com/92-control-color-in-seaborn-heatmaps

https://www.python-graph-gallery.com/92-control-color-in-seaborn-heatmaps

https://www.geeksforgeeks.org/pandas-groupby/

https://www.section.io/engineering-education/seaborn-tutorial/

https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html

https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82

https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda
https://towardsdatascience.com/
getting-more-value-from-the-pandas-value-counts-aa17230907a6

https://pythonbasics.org/seaborn-boxplot/


