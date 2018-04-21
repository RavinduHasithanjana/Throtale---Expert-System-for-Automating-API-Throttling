# copyright reserver for Throtale system
# Authour Ravindu Perera
import pandas as pd
import numpy
from sklearn import svm
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score

# using pandas get the occuring no and the count for the data set


df = pd.read_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv',header=None)
# print(df)
# df.groupby([0]).size().reset_index(name="count").to_csv('/Users/ravinduperera/Desktop/IIT/Research/Development/Dev/csvfile.csv')
cc = df.groupby([0]).size().reset_index(name="count")

# print(cc.iloc[:,1])

data = numpy.array(cc.iloc[:,0]).astype(float)
target = numpy.array(cc.iloc[:,-1]).astype(float)
# print(data.shape)
# print(target.shape)
# #
X = data[:9000]
y = target[:9000]

# print(X)
# print(y)



X_train, X_test, y_train, y_test = train_test_split(
    X.reshape(-1,1), y, test_size=0.25, random_state=0)

parameters = [{'kernel': ['rbf'],
               'gamma': [1e-4, 1e-3, 0.01, 0.1, 0.2, 0.5],
                'C': [1, 10, 100, 1000]},{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]


clf = GridSearchCV(svm.SVC(decision_function_shape='ovr'), parameters, cv=5)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)

print(pred)

acc = accuracy_score(pred,y_test)

print(acc)

print("/////////////////////////////////")

print(clf.best_params_)
print()
print("Grid scores on training set:")
print()
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"
          % (mean, std * 2, params))