import pandas as pd
import tensorflow as tf

# 파일들로 부터 데이터 불러오기
file = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
lemonade = pd.read_csv(file)

file = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston = pd.read_csv(file)

file = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris = pd.read_csv(file)

# 데이터 모양으로 확인하기
print(lemonade.shape)
print(boston.shape)
print(iris.shape)

# 칼럼이름 출력
print(lemonade.columns)
print(boston.columns)
print(iris.columns)

x = lemonade[['온도']]
y = lemonade[['판매량']]
print(x.shape, y.shape)

x = boston[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']]
y = boston[['medv']]
print(x.shape, y.shape)

x = iris[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
y = iris[['품종']]
print(x.shape, y.shape)

lemonade.head() #5개의 값을 볼 수 있음
