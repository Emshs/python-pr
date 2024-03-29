from sklearn import datasets

from sklearn.datasets import load_wine

wine = load_wine()
wine

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=109)

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

from sklearn import metrics

print("정확도:", metrics.accuracy_score(y_test, y_pred))
