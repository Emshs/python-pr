from google.colab import files
uploaded = files.upload()

import pandas as pd
df = pd.read_csv("predict_price.csv", encoding = 'cp949')
df.head()

data=df.drop(['지점'], axis=1)
data.head()

data.info()

set_data=data.dropna(axis=0)
set_data.info()

set_data=data.dropna(axis=0)
set_data=set_data.drop(['날짜'], axis=1)

set_data.info()

set_data.columns = ['Temperature', 'Price', 'Rain_Amount']

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(figsize = (20,8))
ax1.plot(set_data.Temperature, color = 'r', label='Temperature')
ax1.plot(set_data.Rain_Amount, color = 'b', label='Rain_Amount')
ax1.set_ylabel("Temperature & Rain Amount", fontsize=14)
plt.legend(fontsize=14)

ax2 = ax1.twinx()
ax2.plot(set_data.Price, color='g')
ax2.set_ylabel("Cucumber Price", color='g', fontsize=14)

plt.show()

from sklearn.model_selection import train_test_split
x=set_data[['Rain_Amount','Temperature']]
y=set_data['Price']
X_train, X_test, Y_train, Y_test =\
train_test_split(x,y, train_size=0.8, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
mlr_model = LinearRegression()
mlr_model.fit(X_train, Y_train)
rain = int( input('강수량(mm) : '))
temperature = int ( input('온도 (℃) : '))

prediction = mlr_model.predict([[rain, temperature]])

print('강수량 {}mm, 온도 {}℃ 인 경우 예상 오이 가격 : {:7.2f} 원입니다.'.format(rain, temperature, prediction[0]))  #온도30, 강수량30인 경우

accuracy=round(mlr_model.score(X_train, Y_train)*100,2)
print('정확도:', accuracy, '%')

from sklearn import tree
mlr_model = tree.DecisionTreeClassifier()
mlr_model.fit(X_train, Y_train)
rain = int( input('강수량(mm) : '))
temperature = int ( input('온도 (℃) : '))

prediction = mlr_model.predict([[rain, temperature]])

print('강수량 {}mm, 온도 {}℃ 인 경우 예상 오이 가격 : {:7.2f} 원입니다.'.format(rain, temperature, prediction[0]))  #온도30, 강수량30인 경우

accuracy=round(mlr_model.score(X_train, Y_train)*100,2)
print('정확도:', accuracy, '%')
