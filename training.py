from keras import layers
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow.keras.models import Sequential

size = 256

model = Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(size, size, 3)),
    layers.MaxPooling2D(pool_size=(2, 2)),

    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dropout(0.5),

    layers.Dense(128, activation='relu'),
    layers.Dense(2, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=45,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.2,
    zoom_range=0.4,
    horizontal_flip=True)

validation_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory('data/train', target_size=(size, size),
                                                    batch_size=32, class_mode='binary')

validation_generator = validation_datagen.flow_from_directory('data/valid', target_size=(size, size),
                                                              batch_size=32, class_mode='binary')
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=20
)

model.save('new_model.h5')
