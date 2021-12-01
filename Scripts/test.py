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

print(input_data[0,0,:])
print(input_data[0,-1,:])

print(input_data[1,0,:])
print(input_data[1,-1,:])