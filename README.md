# pandsproject


this is the project for the pands module in ATU. 

# <h1> the modules used are as followed  used will be as followed <h1> #

matplotlib this is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms
seaborn this is used for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. It provides a high-level interface for creating nice looking and informative plots. It has many useful features for examining relationships between multiple variables such as those in the Iris dataset.
pandas this provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. It is designed for working with data that is in a tabular format containing an ordered collection of columns where each column can have a different value type. This makes it ideal for exploring a structured tabular dataset such as Iris which contains several numerical columns and one categorical column.
numpy  the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object

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

Once I had this information I wanted to output for detailed information on the dataframe I did this using the describe command, I then returned information on columns and rows that had missing information and duplicated information. 

I used the following code to do this 
 print(iris.describe())
 print(iris.isnull().sum())
 print (iris[iris.duplicated()]) 

 once I had this information I wanted to get the information on the mean max and medain information of each iris class in the dataframe, 

 I used the following code to achieve this 
 print(iris.median()) 
 print(iris.mean())
 print(iris.max())

 once I had this information outputted I closed off the text file. 

 the following information is displayed in a text file. 

 


************************* ANALYSIS OF THE IRIS DATASET *************************



************************* basic information on the dataset*********************/n/n
the columns for this dataset are as follows
Index(['sepal_Length', 'sepal_Width', 'Petal_Length', 'Petal_Width', 'Class'], dtype='object')
printing the first 10 rows of data of the dataset
   sepal_Length  sepal_Width  Petal_Length  Petal_Width        Class
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa
5           5.4          3.9           1.7          0.4  Iris-setosa
6           4.6          3.4           1.4          0.3  Iris-setosa
7           5.0          3.4           1.5          0.2  Iris-setosa
8           4.4          2.9           1.4          0.2  Iris-setosa
9           4.9          3.1           1.5          0.1  Iris-setosa
printing the final 10 rows of the dataset
     sepal_Length  sepal_Width  Petal_Length  Petal_Width           Class
140           6.7          3.1           5.6          2.4  Iris-virginica
141           6.9          3.1           5.1          2.3  Iris-virginica
142           5.8          2.7           5.1          1.9  Iris-virginica
143           6.8          3.2           5.9          2.3  Iris-virginica
144           6.7          3.3           5.7          2.5  Iris-virginica
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica
     sepal_Length  sepal_Width  Petal_Length  Petal_Width            Class
103           6.3          2.9           5.6          1.8   Iris-virginica
144           6.7          3.3           5.7          2.5   Iris-virginica
136           6.3          3.4           5.6          2.4   Iris-virginica
1             4.9          3.0           1.4          0.2      Iris-setosa
63            6.1          2.9           4.7          1.4  Iris-versicolor
    sepal_Length  sepal_Width  Petal_Length  Petal_Width        Class
20           5.4          3.4           1.7          0.2  Iris-setosa
21           5.1          3.7           1.5          0.4  Iris-setosa
22           4.6          3.6           1.0          0.2  Iris-setosa
23           5.1          3.3           1.7          0.5  Iris-setosa
24           4.8          3.4           1.9          0.2  Iris-setosa
25           5.0          3.0           1.6          0.2  Iris-setosa
26           5.0          3.4           1.6          0.4  Iris-setosa
27           5.2          3.5           1.5          0.2  Iris-setosa
28           5.2          3.4           1.4          0.2  Iris-setosa
29           4.7          3.2           1.6          0.2  Iris-setosa

**************************summery of the dataset**********************************/n/n
The following are the three class or species types of iris in the data set 
 Iris-setosa Iris-versicolor Iris-virginica
       sepal_Length  sepal_Width  Petal_Length  Petal_Width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

***The number of null or missing values in the iris dataframe for each column**********
 
sepal_Length    0
sepal_Width     0
Petal_Length    0
Petal_Width     0
Class           0
dtype: int64

=============================== Duplicate Entries==============================

     sepal_Length  sepal_Width  Petal_Length  Petal_Width           Class
34            4.9          3.1           1.5          0.1     Iris-setosa
37            4.9          3.1           1.5          0.1     Iris-setosa
142           5.8          2.7           5.1          1.9  Iris-virginica

============================= Median of Attributes ===========================

sepal_Length    5.80
sepal_Width     3.00
Petal_Length    4.35
Petal_Width     1.30
dtype: float64

******************************Mean of Attributes******************************/n
sepal_Length    5.843333
sepal_Width     3.054000
Petal_Length    3.758667
Petal_Width     1.198667
dtype: float64

******************************Max of Attributes******************************/n
sepal_Length               7.9
sepal_Width                4.4
Petal_Length               6.9
Petal_Width                2.5
Class           Iris-virginica
dtype: object

# Visualising the Iris data set # 

In this section I will discuss visulising the dataset, the first plot I created was a histogram, This histogram returned the Petal length petal width sepal length and sepal width, The histogram for the petal lengths show a clear group of observations having petal lengths that are much smaller than the rest of the observations and similarly so with the petal widths. The sepal lengths show quite a bit of variation with a number of peaks while sepal widths seem to be centred around 3 cms but with a few smaller peaks at both sides of 3 cms. To create this hsitogram I used the following the code. 

iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.suptitle("Histogram of the Iris petal and sepal measurements")
plt.show()

The next visualtion I ran was to get the breakdown of each class using seaborn, this should show that there is exactly 50 per count for each class. I used the following code to achieve this 
sns.set(style="ticks", palette="pastel")
plt.title('Class Count')
sns.countplot(iris['Class'])

I then used a boxplot again using seaborn to show various statistics in one go, including the median, quantiles, interquartile range, outliers etc. The length of the box is the interquartile range and measures the variability in the data set. The interquartile range (IQR) is the middle 50% of the data and can show the spread or variation of the data. The whiskers show if the data is skewed in one direction or the other. The median is the line through the box.

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
Plot 2 shows that there is even higher overlap between the species on sepal width, so it is not an effective Classification feature
Plot 3 shows that petal length is a good Classification feature as it clearly separates the species . The overlap is extremely less (between Versicolor and Virginica) , Setosa is well separated from the rest two
Just like Plot 3, Plot 4 also shows that petal width is a good Classification feature . The overlap is significantly less (between Versicolor and Virginica) , Setosa is well separated from the rest two

the last plot I wanted to create was a scatter plot to show the comparsion between the length and width of each class. 

I used the following code to achieve this 
iris = sns.load_dataset('iris')
sns.lmplot( x="petal_length" , y="petal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()



iris = sns.load_dataset('iris')
sns.lmplot( x="sepal_length" , y="sepal_width" , data=iris, fit_reg=False, hue='species' , legend=False)
plt.legend(loc='lower right')
plt.show()

this will show 



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
https://www.section.io/engineering-education/seaborn-tutorial/
https://realpython.com/pandas-groupby/
https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html
https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82
https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda
https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
https://pythonbasics.org/seaborn-boxplot/


