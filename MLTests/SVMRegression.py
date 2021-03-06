# copyright reserver for Throtale system
# Authour Ravindu Perera
import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

def readcsv ():
    df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv', header=None)
    print(df)
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
    X = data[:9000]
    y = target[:9000]

    X_train, X_test, y_train, y_test = train_test_split(
        X.reshape(-1, 1), y, test_size=0.5, random_state=0)

    clf = svm.SVR()
    clf.fit(X_train,y_train)
    SVR(C=1.0, gamma='0.2', kernel='rbf')
    pred = clf.predict(X_test)
    pic = clf.predict(1.515155085000000000e+09)

    print(pic)
    mean = mean_squared_error(y_test, pred)
    print(mean)
    savingmodel(clf)

def savingmodel(clf):
    print("")
    joblib.dump(clf, 'throtale.pkl')

if __name__ == '__main__': readcsv()