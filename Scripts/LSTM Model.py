import numpy as np
import tensorflow as tf
from tensorflow import keras

raw_data = np.load("inputData.npy", allow_pickle = True)
print(raw_data[1].shape) # 1258 for shape

'''
Whole list of 500 stocks is too much data to pass so will prompt user 
asking which x stocks should be trained -> for now will use 1 as proof of concept
'''


input_data = raw_data[:][:6]
returns = raw_data[:][:,-1].reshape(-1,1)
print(returns[0])
print(returns.shape)
print(input_data[0])
print(input_data.shape)

####################################################
'''
Just need to make x data into time series for input
'''
#T x D x N data where T:time steps, D: Features, N:number
t = 10 
d = inputData[0].shape[1]
n = len(inputData[0]) - t

#StandardScalar, .fit and .transform used to standardize data. .fit only used on training data --> num_train is number of training data
num_train = len(inputData[0]) * 2/3
ss = StandardScaler()  #Creates obj
ss.fit(returns[:len(returns/2)])    #this puts data from argument to standard scalar obj --> ex. mean mode, etc
returns = ss.transform(returns).flatten()   #this standardizes data while keeping statistical data

#Initialize Time Series input
x_train = np.zeros(num_train, t, d)
y_train = np.zeros(num_train)

#Fill the time series - > Here I could make it so that
for i in num_train:
    x_train = input
inputLayer = keras.layers.Input(shape = [1, 7])
lstm1 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid', return_sequences = True)(inputLayer) #use of regularizers or initializers? // 4 is for dimentionality of output
lstm2 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid')(lstm1)
dense1 = keras.layers.Dense(100)(lstm2)
dense2 = keras.layers.Dense(50)(dense1)
out = keras.layers.Dense(5)(dense2) #will want to change number of nodes to desired output

model = keras.Model(inputs = inputLayer, outputs = out)
model.compile(optimizer = adam, loss = sigmoid)

model.summary

