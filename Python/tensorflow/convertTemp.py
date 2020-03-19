import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # ignore init warnings
import tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0' # warnings are good now

temp = input("Temperture in Fahrenheit: ")
