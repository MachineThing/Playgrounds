from __future__ import absolute_import, division, print_function, unicode_literals
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # ignore init warnings
import tensorflow as tf
import numpy as np
import tensorflow_datasets as tfds
tfds.disable_progress_bar()
import math
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0' # warnings are good now

dataset, metadata = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
train_ds, test_ds = dataset['train'], dataset['test']

class_names = ['T-Shirt', 'Pants', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Boot']

num_train_ex = metadata.splits['train'].num_examples
num_test_ex = metadata.splits['test'].num_examples

print("Number of training examples: {}\nNumber of test examples: {}".format(num_train_ex, num_test_ex))

def normalize(images, labels):
    images = tf.cast(images, tf.float32)
    images /= 255
    return images, labels

train_ds = train_ds.map(normalize)
test_ds = test_ds.map(normalize)

train_ds = train_ds.cache()
test_ds = test_ds.cache()

print("Building model...")

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28, 1)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10)
])

print("Compiling model...")

model.compile(optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

print("Training model...")

BATCH_SIZE = 32
train_ds = train_ds.cache().repeat().shuffle(num_train_ex).batch(BATCH_SIZE)
test_ds = test_ds.cache().batch(BATCH_SIZE)

model.fit(train_ds, epochs=5, steps_per_epoch=math.ceil(num_train_ex/BATCH_SIZE))

test_loss, test_accuracy = model.evaluate(test_ds, steps=math.ceil(num_test_ex/32))
print('Accuracy on test dataset:', test_accuracy)
