import tensorflow as tf
from tensorflow import keras
import numpy as np

def createModel():

    cols = 62500
    # fix random seed for reproducibility
    np.random.seed(7)
    # create model
    model = keras.Sequential([
    keras.layers.Dense(250, input_dim=cols, activation='relu'),
    keras.layers.Dense(200, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.softmax)
    ])
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    return model
    

