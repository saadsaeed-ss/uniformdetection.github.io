from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten, Activation, Dropout
from keras.layers import Dense
import tensorflow as tf

import numpy as np

from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img

new_model = Sequential()

new_model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3)))
new_model.add(Activation("relu"))
new_model.add(MaxPooling2D(pool_size=(2, 2)))

new_model.add(Conv2D(32, (3, 3)))
new_model.add(MaxPooling2D(pool_size=(2, 2)))
new_model.add(Activation("relu"))

new_model.add(MaxPooling2D(pool_size=(2, 2)))

new_model.add(Flatten())  # Flattening

new_model.add(Dense(units=64, activation='relu'))
new_model.add(Dense(units=2, activation='softmax'))
new_model.add(Activation("relu"))
new_model.add(Dropout(0.5))

new_model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

new_model.summary()

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(
    rescale=1. / 255)

training = train_datagen.flow_from_directory(
    'Dataset/Training',
    target_size=(64, 64),
    batch_size=12,
    class_mode='binary')

test = test_datagen.flow_from_directory(
    'Dataset/Test',
    target_size=(64, 64),
    batch_size=12,
    class_mode='binary')

new_model.fit(
    training,
    validation_data=test,
    epochs=5
)

new_model.save('model.h5')

img_path = 'Dataset/Predict/p1.jpg'


def predict(file):
    pimg = load_img(
        file,
        target_size=(64, 64)
    )
    pimg = img_to_array(pimg)
    pimg = np.expand_dims(pimg, axis=0)
    predictions = new_model.predict(pimg)
    result = predictions[0]
    if result[0][0] == 1:
        an = 'Uniform'
    else:
        an = 'Non-Uniform'
    return an


res = predict(img_path)
print(res)
