import pandas as pd
import numpy
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split,GridSearchCV
# using pandas get the occuring no and the count for the data set
from sklearn.svm import LinearSVC


df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv',header=None)
print(df)
# df.groupby([0]).size().reset_index(name="count").to_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv')
cc = df.groupby([0]).size().reset_index(name='counts')

print(cc)