import numpy as np
import tensorflow as tf
from tensorflow import keras

inputData = np.load("inputData.npy", allow_pickle = True)
#print(inputData[1].shape) --> 1259 for shape

inputLayer = keras.layers.Input(shape = [1, 7])
lstm1 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid', return_sequences = True)(inputLayer) #use of regularizers or initializers? // 4 is for dimentionality of output
lstm2 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid')(lstm1)
dense1 = keras.layers.Dense(100)(lstm2)
dense2 = keras.layers.Dense(50)(dense1)
out = keras.layers.Dense(5)(dense2) #will want to change number of nodes to desired output

model = keras.Model(inputs = inputLayer, outputs = out)
model.summary

