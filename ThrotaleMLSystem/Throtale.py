import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.externals import joblib
import time
import sys
import threading



def predictions():
    print("work")
    # millis = float(round(time.time() * 1000))
    # print(millis)
    clf = joblib.load('Final.pkl')
    # print("work")
    preictioMade = clf.predict([[16., 12., 22., 12., 24.]])
    print("work")
    # add the time for the prediction model so the script will run

    print(str(preictioMade))
    # threading.Timer(1.0, predictions).start()
# 1.513444888000000000e+09
# def retrainers():



if __name__ == '__main__': predictions()