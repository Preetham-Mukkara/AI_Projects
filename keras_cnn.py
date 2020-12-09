#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:20:23 2020

@author: Preetham Mukkara
"""
import tensorflow as tf
from tensorflow import keras
import numpy as np

def get_dataset(training=True):
    fashion_mnist = keras.datasets.fashion_mnist
    train,test = fashion_mnist.load_data()  
    if training is True:
        #return training images and labels once resized
        return (np.reshape(train[0], (60000, 28, 28, 1)),train[1])
    else:
        #return testing images and labels once resized
        return (np.reshape(test[0],(10000, 28, 28, 1)),test[1])
    
def build_model():
    #adds two 2D convolutional layer, a flatten layer and a dense layer
    model = keras.Sequential([tf.keras.layers.Conv2D(64, 3, activation='relu', input_shape=(28, 28, 1)),
                              tf.keras.layers.Conv2D(32, 3, activation='relu'),
                              tf.keras.layers.Flatten(),
                              tf.keras.layers.Dense(10, activation='softmax')])
    #compiles with categorical_crossentropy
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_model(model, train_img, train_lab, test_img, test_lab, T):
    #trains the model
    train_labels = keras.utils.to_categorical(train_lab)
    test_labels = keras.utils.to_categorical(test_lab)
    model.fit(x=train_img, y=train_labels, epochs=T, validation_data=(test_img, test_labels))
    
def predict_label(model, images, index):
    temp1 = model.predict(images)
    temp2 = temp1[index]
    temp = temp2
    
    #takes top three values
    temp = temp.argsort()[-3:][::-1]
    
    #iterate through array
    for i in range(len(temp)):
        if(0 == temp[i]):
          print('T-shirt/top: ' + str(round(temp2[temp[i]]*100, 2)) + '%')
        elif(1 == temp[i]):
          print('Trouser: ' + str(round(temp2[temp[i]]*100, 2)) + '%')
        elif(2 == temp[i]):
          print('Pullover: ' + str(round(temp2[temp[i]]*100, 2))  + '%')
        elif(3 == temp[i]):
          print('Dress: ' + str(round(temp2[temp[i]]*100, 2))  + '%')
        elif(4 == temp[i]):
          print('Coat: ' + str(round(temp2[temp[i]]*100, 2))  + '%')
        elif(5 == temp[i]):
          print('Sandal: ' + str(round(temp2[temp[i]]*100, 2))  + '%')
        elif(6 == temp[i]):
          print('Shirt: ' + str(round(temp2[temp[i]]*100, 2))  + '%')
        elif(7 == temp[i]):
          print('Sneaker: ' + str(round(temp2[temp[i]]*100, 2))  + '%')
        elif(8 == temp[i]):
          print('Bag: ' + str(round(temp2[temp[i]]*100, 2))  + '%')
        elif(9 == temp[i]):
          print('Ankle boot: ' + str(round(temp2[temp[i]]*100, 2))  + '%')    