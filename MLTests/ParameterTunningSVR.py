import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV


def readcsv ():
    df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv', header=None)
    print(df)
    # df.groupby([0]).size().reset_index(name="count").to_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv')
    cc = df.groupby([0]).size().reset_index(name='counts')
    print(cc)


def parameterTunning ():
    print()



if __name__ == '__main__': readcsv()