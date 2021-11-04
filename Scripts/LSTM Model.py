import numpy as np
import tensorflow 
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.preprocessing import StandardScaler

raw_data = np.load("inputData.npy", allow_pickle = True)
#print(raw_data[1].shape) 1258 for shape

'''
Whole list of 500 stocks is too much data to pass so will prompt user 
asking which x stocks should be trained -> for now will use 1 as proof of concept

--> index like this, if grabbing data for multiple stocks need loop
'''

''' THIS IS FOR INDEXING DATA USING TICKERS
userinput = ['AAPL']

for i in range(len(raw_data)):
    if raw_data[i][0, 6] in userinput:
        input_data = raw_data[i][:, 1:6]
        returns = raw_data[i][:, -1]
'''
'FOR INDEXING RANDOMLY'

num_stocks = 10 # arbitrary value
userinput = np.random.randint(500, size = (num_stocks)) #taking arbitrary number of random indices for selection from 500 stocks
input_data = np.zeros(num_stocks, raw_data[0].shape[0], 6) # initializing data array of size (num_stocks, number of time steps, number of desire features) 
j = 0 #indexing variable to index input_data and returns

for i in userinput:
    input_data[j, :, :] = raw_data[i][:, 1:6] #splitting features so that features for training are seperate from un-needed features and return values used for labels
    returns = raw_data[i][:, -1]

####################################################
'''
Just need to make x data into time series for input
'''
#N x T x D data where T:time steps, D: Features, N:number of usable times, since need t pieces of data for prediction
t = 10 #number of time stamps for each sequence
d = input_data.shape[1]
n = len(input_data) - t

#StandardScalar, .fit and .transform used to standardize data. .fit only used on training data --> num_train is number of training data
num_train = len(input_data) * 2 // 3
print('Num Train: ', num_train)
ss = StandardScaler()  #Creates obj
ss.fit(input_data[:num_train])    #this puts data from argument to standard scalar obj --> ex. mean mode, etc
input_data = ss.transform(input_data)  #this standardizes data while keeping statistical data

#Initialize Time Series inputs
x_train = np.zeros((num_train, t, d))
y_train = np.zeros(num_train)

x_test = np.zeros((n - num_train, t, d))
y_test = np.zeros(n - num_train)

#Fill the time series
for i in range(num_train):
    x_train[i, :, :] = input_data[i:i+t, :] #this makes each x_train data a range from current index to index + t which gives series
    y_train[i] = (returns[i+t] > 0) #labels are boolean where true when return is positive

for k in range(n - num_train):
    u = k + num_train #k gives the number of test data points, u is the indices for the test data
    x_test[k, :, :] = input_data[u:u+t, :]
    y_test[k] = (returns[u+t] > 0)


inputLayer = keras.layers.Input(shape = [10, 5])
lstm1 = keras.layers.LSTM(5, activation = 'tanh', recurrent_activation = 'sigmoid', return_sequences = True)(inputLayer) #use of regularizers or initializers? // 4 is for dimentionality of output
lstm2 = keras.layers.LSTM(5, activation = 'tanh', recurrent_activation = 'sigmoid')(lstm1)
dense1 = keras.layers.Dense(50)(lstm2)
out = keras.layers.Dense(1, activation = 'sigmoid')(dense1) #will want to change number of nodes to desired output

model = keras.Model(inputs = inputLayer, outputs = out)
model.compile(optimizer = 'adam', loss = 'binary_crossentropy',  metrics = 'accuracy')
model.summary
history = model.fit(x_train, y_train, epochs = 50, validation_data = (x_test, y_test))

print(history.history.keys())

plt.clf()
plt.plot(history.history['accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy [%]')
plt.xlabel('Numbers of Training Epochs')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()



