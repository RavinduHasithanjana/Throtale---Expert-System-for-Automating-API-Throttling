# copyright reserver for Throtale system
# Authour Ravindu Perera
import pandas as pd
import numpy
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV

def readcsv ():
    df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv', header=None)
    print(df)
    # df.groupby([0]).size().reset_index(name="count").to_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv')
    cc = df.groupby([0]).size().reset_index(name='counts')
    regressionalgo(cc)


def regressionalgo (cc):
    data = numpy.array(cc.iloc[:, 0]).astype(float)
    target = numpy.array(cc.iloc[:, -1]).astype(float)
    print(data.shape)
    # print(target.shape)
    # #
    X = data[:100]
    y = target[:100]

    X_train, X_test, y_train, y_test = train_test_split(
        X.reshape(-1, 1), y, test_size=0.5, random_state=0)


if __name__ == '__main__': readcsv()