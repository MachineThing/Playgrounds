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
train_dataset, test_dataset = dataset['train'], dataset['test']
