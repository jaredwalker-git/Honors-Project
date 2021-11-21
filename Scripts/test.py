import itertools
import numpy as np

raw_data = np.load("inputData.npy", allow_pickle = True)
for i in range(len(raw_data)):
    if raw_data[i].shape[0] == 1258:
        
        print(raw_data[i].shape) 