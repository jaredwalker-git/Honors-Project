import itertools
import numpy as np

raw_data = np.load('inputData.npy', allow_pickle = True) 
tickers = ['AAL', 'AAPL']
#initialize array for data at # tickers x timesteps x features -> features are explicitly set since no good way to generalize this aspect for any data
input_data = np.zeros(shape = (len(tickers), raw_data[1].shape[0], 5))
    #j is index for new data, and will be incremented from 0 to num_stocks as tickers are found in raw data
j = 0

for i in range(len(raw_data)):
    if raw_data[i][0, 6] in tickers:
        input_data[j, :, :] = raw_data[i][:, 1:6]
        j = j + 1

num_stocks = input_data.shape[0]
num_timesteps = input_data.shape[1]
num_features = input_data.shape[2]
       
#split to test vs train data
'''
t = 10 #number of time stamps for each sequence                         <THIS MAY BE NECESSARY
n = len(data) - t #length of usable timesteps for series creation
'''

#choosing amount of data for training
num_train = num_timesteps // 2
#Initialize Time Series inputs
train_data = np.zeros(shape = (num_stocks, num_train, num_features))
test_data = np.zeros(shape = (num_stocks, num_train + 1, num_features))

for n in range(num_stocks):
    train_data[n, :, :] = input_data[n, :num_train, :]
    test_data[n, :, :] = input_data[n, num_train:, :]

print(train_data[0,0,:])
print(train_data[0,-1,:])

print(train_data[1,0,:])
print(train_data[1,-1,:])