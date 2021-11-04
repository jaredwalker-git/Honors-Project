import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data():
    #import .csv data and convert to numpy array
    data = "all_stocks_5yr.csv"
    df = pd.read_csv(data)
    
    #now to create return value data for labels
    df['LastClose'] = df['close'].shift(1)
    df['Return'] = (df['close'] - df['LastClose'])/df['close']
    dfArray = df.to_numpy()

    #figuring out size and indices of data
    '''
    print(dfArray[0,6])
    print(dfArray.shape[0])
    '''


    ################################################################################
    #Update code so array is initialized with np.zeros and filled using indexing, 
    #this will make working with data more easy later


    ################################################################################
 
    nameLast = 'AAL'
    timesteps = 0
    rowsPer = 0
    input_data_list = []

    for k in range(dfArray.shape[0]):   #This figures the number of timesteps per stock
        if dfArray[k, 6] == nameLast:
            timesteps = timesteps + 1
    

    data_array = np.zeros(shape = (timesteps,9), dtype = object)
  
    for i in range(dfArray.shape[0]):
        if dfArray[i, 6] == nameLast:
            data_array[rowsPer, :] = dfArray[i,:].reshape(1,9) #reshape of dfArray for dimension matching
            rowsPer = rowsPer + 1
        
        else:
            nameLast = dfArray[i, 6]
            input_data_list.append(data_array[:rowsPer, :])
            #print(data_array[:rowsPer, :].shape)
            data_array = np.zeros(shape = (timesteps,9), dtype = object)
            rowsPer = 0

    inputData = np.array(input_data_list, dtype = object)

    print(inputData[-1])

    '''
    df['Return'].hist(bins = 10)
    plt.show()
    '''

    np.save('inputData.npy', inputData)

load_data() #This will be removed once script is called from another python module

        


'''need to figure which stocks have fewer entries since rn all arrays are initialized to timesteps = 1260 meaning if 1059 is max size for one data will b skewed'''



