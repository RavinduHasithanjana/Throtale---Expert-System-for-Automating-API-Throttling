import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.externals import joblib
import time




def predictions():
    print()
    millis = float(round(time.time() * 1000))
    print(millis)
    clf = joblib.load('throtale.pkl')
    hello = clf.predict(1.513444888000000000e+09)
    print(hello)
# 1.513444888000000000e+09

def retrainers():
    print()


if __name__ == '__main__': predictions()