# copyright reserver for Throtale system
# Authour Ravindu Perera
import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV

def read_analyse_csv ():
  dataframe = pd.read_csv('/Users/ravinduperera/Desktop/GSOC_2017/Dev/Throtale---Expert-System-for-Automating-API-Throttling/LogFiles/ExtractedData.csv', header=None)
  print("vdvdv")



if __name__ == '__main__': read_analyse_csv()