
from sklearn import datasets

from sklearn.datasets import load_breast_cancer

import pandas as pd

import numpy as np

data = datasets.load_breast_cancer()
data

from sklearn.model_selection import train_test_split

df = pd.DataFrame(data.data, columns = data.feature_names)

df= df[['mean radius', 'mean texture', 'mean area', 'mean symmetry']]

df['target'] = data.target

df

X=df[df.columns[:-1]]

y =df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 87)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB(alpha=1.0)

model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print("정확도: ", accuracy_score(y_test, y_pred))

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_test_pca = pca.fit_transform(X_test)

y_find = y_test.reset_index(drop = True)
index_0 = y_find[y_find ==0].index
index_1 = y_find[y_find ==1].index

y_pred_Series = pd.Series(y_pred)
index_0_p = y_pred_Series[y_pred_Series == 0].index
index_1_p = y_pred_Series[y_pred_Series == 1].index

plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.scatter(X_test_pca[index_0, 0], X_test_pca[index_0, 1], color = 'pink', alpha = 0.6, label='malignant')
plt.scatter(X_test_pca[index_1, 0], X_test_pca[index_1, 1], color = 'skyblue', alpha = 0.6, label ='benign')
plt.title('Real target', size = 13)
plt.legend()

plt.subplot(122)
plt.scatter(X_test_pca[index_0_p, 0], X_test_pca[index_0_p, 1], color = 'pink', alpha = 0.6, label='malignant')
plt.scatter(X_test_pca[index_1_p, 0], X_test_pca[index_1_p, 1], color = 'skyblue', alpha = 0.6, label ='benign')
plt.title('NB result', size = 13)
plt.legend()
plt.show()

