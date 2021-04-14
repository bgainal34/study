# 라이브러리
import pandas as pd
import tensorflow as tf
# 데이터 준비
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
데이터 = pd.read_csv(파일경로)
# 종속변수, 독립변수
독립 = 데이터[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']]
종속 = 데이터[['medv']]
# 모델 만들기
X = tf.keras.layers.Input(shape=[13])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')
# 모델 학습하기
model.fit(독립, 종속, epochs=10000)
# 모델 이용하기
print("prediction :", model.predict(독립[0:5]))
print(종속[0:5])
# 모델의 수식 확인
print(model.get_weights())