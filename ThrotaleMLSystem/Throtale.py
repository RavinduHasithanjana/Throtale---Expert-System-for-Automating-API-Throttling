import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.externals import joblib
import time
import sys




def predictions():
    print("started")
    # millis = float(round(time.time() * 1000))
    # print(millis)
    clf = joblib.load('Final.pkl')
    preictioMade = clf.predict([[16., 12., 22., 12., 24.]])

    print(preictioMade)
# 1.513444888000000000e+09

def retrainers():
    print()


if __name__ == '__main__': predictions()