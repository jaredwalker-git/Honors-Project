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
    #print(dfArray[0,6])
    #print(dfArray.shape[0])

    ################################################################################
    #Initializing variables to be used in data preprocessing
    nameLast = 'AAL'
    rowsPer = 0 
    input_data_list = []
    good_data = []
     
    data_array = np.zeros(shape = (2000,9), dtype = object) #initializing a data array here -> integers used to initialize since max time steps is 1258 and trying to initialize with a variable leads to inefficient data allocation
  
    for i in range(dfArray.shape[0]):
        if dfArray[i, 6] != nameLast:
            nameLast = dfArray[i, 6]
            input_data_list.append(data_array[:rowsPer, :]) #only appends the data array up until rowsPer -> this is so same array can be used and anything after this index is N/A
            rowsPer = 0 #set rowsPer to 0 to index first time step of new array for next stock
            data_array = np.zeros(shape = (2000 ,9), dtype = object) #reinitializing here since when this is left out python prints all input_data_list as final stock data -> this was only way to fix error

        data_array[rowsPer, :] = dfArray[i,:].reshape(1,9) 
        rowsPer = rowsPer + 1 

    input_data_list.append(data_array[:rowsPer, :]) #to append the last timestep of dfArray
    for i in range(len(input_data_list)):
        #only pass data with 1259 data points as this keeps later data simple
        if input_data_list[i].shape[0] == 1259:
            good_data.append(input_data_list[i])
            print(input_data_list[i])

    inputData = np.array(good_data, dtype = object)    
    np.save('inputData.npy', inputData)

    
load_data() #This will be removed once script is called from another python module

        


'''need to figure which stocks have fewer entries since rn all arrays are initialized to timesteps = 1260 meaning if 1059 is max size for one data will b skewed'''



