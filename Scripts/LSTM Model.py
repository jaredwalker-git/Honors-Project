import numpy as np
import tensorflow as tf
from tensorflow import keras

inputData = np.load("inputData.npy", allow_pickle = True)
#print(inputData[1].shape) --> 1259 for shape

returns = inputData[:,-1].values[1:].reshape(-1,1)
####################################################
'''
Just need to make x data into time series for input
'''

#StandardScalar, .fit and .transform used to standardize data. .fit only used on training data
ss = StandardScaler()
ss.fit(returns[:len(returns/2)])
returns = ss.transform(returns).flatten()

inputLayer = keras.layers.Input(shape = [1, 7])
lstm1 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid', return_sequences = True)(inputLayer) #use of regularizers or initializers? // 4 is for dimentionality of output
lstm2 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid')(lstm1)
dense1 = keras.layers.Dense(100)(lstm2)
dense2 = keras.layers.Dense(50)(dense1)
out = keras.layers.Dense(5)(dense2) #will want to change number of nodes to desired output

model = keras.Model(inputs = inputLayer, outputs = out)
model.compile(optimizer = adam, loss = sigmoid)

model.summary

