# 라이브러리
import pandas as pd
import tensorflow as tf
# 데이터 준비
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
데이터 = pd.read_csv(파일경로)
# 종속변수, 독립변수
독립 = 데이터[['온도']]
종속 = 데이터[['판매량']]
# 모델 만들기
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')
# 모델 학습하기
model.fit(독립, 종속, epochs=10000)
# 모델 이용하기
print(model.predict([15]))