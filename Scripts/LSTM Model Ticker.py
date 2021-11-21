import numpy as np
import tensorflow 
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.preprocessing import StandardScaler

raw_data = np.load("inputData.npy", allow_pickle = True)

'''
Just need to make x data into time series for input
'''
ticker = ['AAPL']
input_data = raw_data[:, 1:6]
returns = raw_data[i][:, -1]
#N x T x D data where T:time steps, D: Features, N:number of usable times, since need t pieces of data for prediction
num_features = 5 #number of chosen features
t = 10 #number of time stamps for each sequence
d = num_features
n = len(input_data) - t


#StandardScalar, .fit and .transform used to standardize data. .fit only used on training data --> num_train is number of training data
num_train = len(input_data) * 2 // 3
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


inputLayer = keras.layers.Input(shape = [10, num_features])
lstm1 = keras.layers.LSTM(num_features, activation = 'tanh', recurrent_activation = 'sigmoid', return_sequences = True)(inputLayer) #use of regularizers or initializers? // 4 is for dimentionality of output
lstm2 = keras.layers.LSTM(num_features, activation = 'tanh', recurrent_activation = 'sigmoid')(lstm1)
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



