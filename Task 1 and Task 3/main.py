from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Activation, Dropout
from keras.layers import Dense
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
from keras import callbacks
import os.path
from keras.preprocessing.image import ImageDataGenerator

new_model = Sequential()

new_model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3)))  # Layer 1 Convolution and Pooling
new_model.add(Activation("relu"))
new_model.add(MaxPooling2D(pool_size=(2, 2)))

new_model.add(Conv2D(32, (3, 3)))  # Layer 2 - Convolution and Pooling
new_model.add(MaxPooling2D(pool_size=(2, 2)))
new_model.add(Activation("relu"))
new_model.add(MaxPooling2D(pool_size=(2, 2)))

new_model.add(Flatten())  # Flattening

new_model.add(Dense(units=128, activation='relu'))  # Full connection
new_model.add(Dense(units=1, activation='softmax'))
new_model.add(Activation("relu"))
new_model.add(Dropout(0.5))

new_model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])  # Compiling  Model

new_model.summary()

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)  # Fitting the CNN to the images

test_datagen = ImageDataGenerator(
    rescale=1. / 255)

training_set = train_datagen.flow_from_directory(
    'Dataset/Training',
    target_size=(64, 64),
    batch_size=12,
    class_mode='binary')
test_set = test_datagen.flow_from_directory(
    'Dataset/Test',
    target_size=(64, 64),
    batch_size=12,
    class_mode='binary')

