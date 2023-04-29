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
The Iris Data Set is available from the UC Irvine Machine Learning Repository at http://archive.ics.uci.edu/ml/datasets/Iris in csv. I used the following code to achieve this. 

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

the first part of this project involves looking at the dataset and investagating it. I begin by setting up some print statements to check was the dataset loaded and also to allow me to return some data. I used the pandas module for this as it has a lot of great libries that can be used for exploring data. I began by looking at the number of the axes and dimionsions in the dataset I used the ndim atturibute to do this. I then used the shape attriubte to return information about axis dimensions of the the number or rows and columns in the table of data. This will show how many rows (containing observations) and columns (containing features/variables) in the Iris Data set. I then returned the size of the elements in the dataset using the size attrubute to return this. I then used the index atturibute to show the index which was automatically assigned when the dataFrame was created on reading in the csv file this gave the information on the columns and rows of the dataset. I then used the head and tail attrubute to return the first and last 10 elements of the dataset, this showed that I downloaded the CSV correctly. 

# <p> the next step was to output infomration to a text file <p> # 


