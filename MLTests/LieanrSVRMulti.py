#paramter tunning fo the new datset with multiple features

import pandas as pd
import numpy
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.svm import LinearSVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV


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

    clf = svm.LinearSVR()
    clf.fit(X_train, y_train)
    LinearSVR(C=1.0, dual=True, epsilon=0.0, fit_intercept=True,
     intercept_scaling=1.0, loss='epsilon_insensitive', max_iter=1000,
     random_state=0, tol=0.0001, verbose=0)
    pred = clf.predict(X_test)

    # print(clf.best_params_)
    print("/////////////////")
    mean = mean_squared_error(y_test, pred)
    print(mean)


    print()

    # means = clf.cv_results_['mean_test_score']
    # stds = clf.cv_results_['std_test_score']
    # for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    #     print("%0.3f (+/-%0.03f) for %r"
    #           % (mean, std * 2, params))


def savingModel ():
    print()



if __name__ == '__main__': readcsv()