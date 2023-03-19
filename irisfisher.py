#importing the modlues to begin the project

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd


cols = ['sepal_Length', 'sepal_Width','Petal_Length','Petal_Width','Class']
csv = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#reading the CSV file 
iris =  pd.read_csv(csv, names = cols)
#returning the first ten rows of data to ensure that the file has loaded correctly
print(iris.head(10))

