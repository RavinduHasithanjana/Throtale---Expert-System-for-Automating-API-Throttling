import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.externals import joblib



def predictions():
    print()
    clf = joblib.load('throtale.pkl')
    hello = clf.predict(1527006867)
    print(hello)


def retrainers():
    print()


if __name__ == '__main__': predictions()