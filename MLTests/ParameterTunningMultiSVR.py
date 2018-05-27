#paramter tunning fo the new datset with multiple features

import pandas as pd
import numpy
from sklearn.svm import SVR
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV


def readcsv ():
    df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv', header=None)
    formatData = df.groupby([0]).size().reset_index(name='counts')
    print(formatData)
    parameterTunning(formatData)


def parameterTunning (formatData):
    dataData = numpy.array(formatData.iloc[:, 0]).astype(float)
    targetData = numpy.array(formatData.iloc[:, -1]).astype(float)

    X = dataData[:1000]
    y = targetData[:1000]


    X_train, X_test, y_train, y_test = train_test_split(
        X.reshape(-1, 1), y, test_size=0.25, random_state=0)

    parameters = [{'kernel': ['rbf'],
                   'gamma': [1e-4, 1e-3, 0.01, 0.1, 0.2, 0.5],
                   'C': [1, 10, 100, 1000]}]

    print("parameter tunning")
    clf = GridSearchCV(svm.SVR(), parameters, cv=5)
    clf.fit(X_train, y_train)
    print("done")
    print(clf.best_params_)
    print("/////////////////")


    print()

    # means = clf.cv_results_['mean_test_score']
    # stds = clf.cv_results_['std_test_score']
    # for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    #     print("%0.3f (+/-%0.03f) for %r"
    #           % (mean, std * 2, params))


def savingModel ():
    print()



if __name__ == '__main__': readcsv()