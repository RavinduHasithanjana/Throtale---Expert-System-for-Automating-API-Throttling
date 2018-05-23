# copyright reserver for Throtale system
# Authour Ravindu Perera
import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import explained_variance_score, accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib
from LogsExtraction import  LogsExtraction

# def logsextraction():
#     LogsExtraction.LogsExtraction()
#     print("done")
#     readcsv()

def readcsv ():
    df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv', header=None)
    day = pd.read_csv('/Users/ravinduperera/Desktop/GSOC_2017/Dev/Throtale---Expert-System-for-Automating-API-Throttling/LogsExtraction/ExtractedDataDay.csv', header=None)
    print(day)
    # df.groupby([0]).size().reset_index(name="count").to_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv')
    cc = df.groupby([0]).size().reset_index(name='counts')
    print(cc)
    regressionalgo(cc)


def regressionalgo (cc):
    data = numpy.array(cc.iloc[:, 0]).astype(float)
    target = numpy.array(cc.iloc[:, -1]).astype(float)
    print(data.shape)
    # print(target.shape)
    # #
    X = data[:10000]
    y = target[:10000]

    X_train, X_test, y_train, y_test = train_test_split(
        X.reshape(-1, 1), y, test_size=0.5, random_state=0)

    clf = svm.SVR()
    clf.fit(X_train,y_train)
    svm.SVR(C=1,kernel='rbf',gamma=0.5)
    pred = clf.predict(X_test)
    prd = clf.predict(1.513444888000000000e+09)
    print(prd)

    # print(pred)
    # acc = accuracy_score(pred, y_test)
    # print(acc)
    savingmodel(clf)

def savingmodel(clf):
    print("")
    joblib.dump(clf, 'throtale.pkl')

if __name__ == '__main__': readcsv()