# copyright reserver for Throtale system
# Authour Ravindu Perera
import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import explained_variance_score, accuracy_score, median_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib
from LogsExtraction import  LogsExtraction

# def logsextraction():
#     LogsExtraction.LogsExtraction()
#     print("done")
#     readcsv()

def readcsv ():
    df = pd.read_csv('/Users/ravinduperera/Desktop/GSOC_2017/Dev/Throtale---Expert-System-for-Automating-API-Throttling/LogsExtraction/ExtractedDataMon.csv', header=None,dtype=str)
    print(df)
    cc = df.groupby([5]).size().reset_index(name='counts')
    df1 = df.drop_duplicates(subset=[5])

    print(df1)
    regressionalgo(cc,df1)


def regressionalgo (cc,df):
    data = numpy.array(df.iloc[:,:5]).astype(float)
    target = numpy.array(cc.iloc[:, -1]).astype(float)
    print(data)
    print(data.shape)

    print(target.shape)

    X = data[:10000]
    y = target[:10000]

    X_train, X_test, y_train, y_test = train_test_split(
        X.reshape(-1, 5), y, test_size=0.5, random_state=0)

    clf = svm.SVR()
    clf.fit(X_train,y_train)
    svm.SVR(C=1,kernel='rbf',gamma=0.5)
    pred = clf.predict(X_test)
    prd = clf.predict([[16., 12., 22., 12., 24.]])
    print(prd)

    mean = mean_squared_error(y_test, pred)
    print("")
    print(mean)
    ex = median_absolute_error(y_test, pred)
    print("")
    print(ex)
    #
    # # print(pred)
    # # acc = accuracy_score(pred, y_test)
    # # print(acc)
    # savingmodel(clf)

def savingmodel(clf):
    print("")
    joblib.dump(clf, 'throtale.pkl')

if __name__ == '__main__': readcsv()