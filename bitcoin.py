import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
import datetime

data = pd.read_csv('C:/Users/tler0/Desktop/통합 문서1.csv')

high_price = data['고가'].values
low_price = data['저가'].values
mid_price = (high_price+low_price)/2

seq_len = 50
sequence_length = seq_len + 1
result = []
for index in range(len(mid_price) - sequence_length):
    result.append(mid_price[index: index + sequence_length])

normalized_data = []
for window in result:
    normalized_window = [((float(p)/float(window[0]))-1)for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

row = int(round(result.shape[0]*0.9))
train = result[:row, :]
np.random.shuffle(train)

x_train = train[:, :-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer='rmsprop')

model.fit(x_train, y_train,
          validation_data=(x_test, y_test),
          batch_size=10,
          epochs=20)

pred = model.predict(x_test)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y_test, label='True')
ax.plot(pred, label='Prediction')
ax.legend()
plt.show()