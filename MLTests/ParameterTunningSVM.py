# copyright reserver for Throtale system
# Authour Ravindu Perera
import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV

def read_analyse_csv ():
  df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv', header=None)