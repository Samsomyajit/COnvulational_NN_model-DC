# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:05:05 2018

@author: Sam
"""

#Convolutional Neural Network

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initializing the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(filters = 32, kernel_size = 3, input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a 2nd convolutional layer
classifier.add(Convolution2D(filters = 32, kernel_size = 3, data_format = "channels_last", activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full Connection
classifier.add(Dense(128, activation = 'relu'))
classifier.add(Dense(1, activation = 'sigmoid'))
# used activation function soft max for non binary output, and siqmoid for binary output

# Compiling the CNN
classifier.compile('adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# for binary outcome choose loss function as binary cross entropy, and for non binary use categorical cross entropy

# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(training_set,
                         steps_per_epoch=8000/32,
                         epochs=25,
                         validation_data=test_set,
                         validation_steps=2000/32)
#classification_st model 1356Z
