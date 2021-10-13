import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import StandardScaler

raw_data = np.load("inputData.npy", allow_pickle = True)
print(raw_data[1].shape) # 1258 for shape

'''
Whole list of 500 stocks is too much data to pass so will prompt user 
asking which x stocks should be trained -> for now will use 1 as proof of concept

--> index like this, if grabbing data for multiple stocks need loop
'''

userinput = ['AAPL']

for i in range(len(raw_data)):
    if raw_data[i][0, 6] in userinput:
        input_data = raw_data[i][:, :7]
        returns = raw_data[i][:, -1]

####################################################
'''
Just need to make x data into time series for input
'''
#N x T x D data where T:time steps, D: Features, N:number of usable times, since need t pieces of data for prediction
t = 10 
d = input_data[0].shape[1]
n = len(input_data[0]) - t

#StandardScalar, .fit and .transform used to standardize data. .fit only used on training data --> num_train is number of training data
num_train = len(input_data[0]) * 2/3
ss = StandardScaler()  #Creates obj
ss.fit(input_data[:num_train])    #this puts data from argument to standard scalar obj --> ex. mean mode, etc
input_data = ss.transform(input_data)  #this standardizes data while keeping statistical data
print(input_data[1])

#Initialize Time Series inputs
x_train = np.zeros(num_train, t, d)
y_train = np.zeros(num_train)

x_test = np.zeros(n - num_train, t, d)
y_test = np.zeros(n - num_train)

#Fill the time series
for i in num_train:
    x_train[i, :, :] = input_data[i:i+t, :] #this makes each x_train data a range from current index to index + t which gives series
    y_train[i] = (returns[i+t] > 0) #labels are boolean where true when return is positive

for k in range(n - num_train):
    u = k + num_train #k gives the number of test data points, u is the indices for the test data
    x_test[k, :, :] = input_data[u + t, :, :]
    y_test[k] = (returns[u+t] > 0)


inputLayer = keras.layers.Input(shape = [1, 7])
lstm1 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid', return_sequences = True)(inputLayer) #use of regularizers or initializers? // 4 is for dimentionality of output
lstm2 = keras.layers.LSTM(7, activation = 'tanh', recurrent_activation = 'sigmoid')(lstm1)
dense1 = keras.layers.Dense(100)(lstm2)
dense2 = keras.layers.Dense(50)(dense1)
out = keras.layers.Dense(5)(dense2) #will want to change number of nodes to desired output

model = keras.Model(inputs = inputLayer, outputs = out)
model.compile(optimizer = adam, loss = sigmoid)

model.summary

