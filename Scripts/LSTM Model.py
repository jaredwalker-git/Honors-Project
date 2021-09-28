import numpy as np

inputData = np.load("inputData.npy", allow_pickle = True)
print(inputData[1])
print(inputData[-1])

'''
inputLayer = keras.layers.Input(shape = TBD)
lstm1 = keras.layers.LSTM(4, activation = 'tanh', recurrent_activation = 'sigmoid')(input) #use of regularizers or initializers? // 4 is for dimentionality of output
drop1 = keras.layers.Dropout()(lstm1)
lstm2 = keras.layers.LSTM(4, activation = 'tanh', recurrent_activation = 'sigmoid')(drop1)
dense1 = keras.layers.Dense(100)(lstm2)
dense2 = keras.layers.Dense(50)(dense1)
out = keras.layers.Dense(5)(dense2) #will want to change number of nodes to desired output

model = keras.Model(inputs = inputLayer, outputs = out)
model.summary
'''