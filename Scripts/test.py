import numpy as np

raw_data = np.load('inputData.npy', allow_pickle = True) 
tickers = ['AAPL']
#initialize array for data at # tickers x timesteps x features
input_data = np.zeros(shape = (len(tickers), raw_data[0].shape[0], 5))
print(len(tickers))
j = 0

for i in range(len(raw_data)):
    print(i)
    if raw_data[i][0, 6] in tickers:
        print(raw_data[i][0, 6])
        print(raw_data[i])
        input_data[j, :, :] = raw_data[i][:, 1:6]
        j = j + 1
    