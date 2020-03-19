import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # ignore init warnings
import tensorflow as tf
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0' # warnings are good now

# Ask user for temperture
gotTemp = False
while not gotTemp:
    try:
        temp = float(input('Temperture in Fahrenheit: '))
        gotTemp = True
    except ValueError:
        print('Invalid temperture')

del(gotTemp)

# Training values
cels_t = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahr_t = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
print('Made training values:\ncels_t: {}\nfahr_t: {}'.format(cels_t, fahr_t))

# Create a model
print('Creating model...')
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
print('Compiling model...')
model.compile(
    loss='mean_squared_error',
    optimizer=tf.keras.optimizers.Adam(0.15)
)
45
# Train model
print('Training model...')
history = model.fit(fahr_t, cels_t, epochs=500, verbose=False)

# Predict value and ask user if they want to see training results
res = model.predict([temp])
print('I think your temperture in celsius is {}!'.format(res))
while True:
    tdisp = input('Would you like to see my training stats? Y/N: ').lower()
    if tdisp == 'y':
        import matplotlib.pyplot as plt
        plt.xlabel('Epoch Number')
        plt.ylabel("Loss Magnitude")
        plt.plot(history.history['loss'])
        plt.show()
        break
    elif tdisp == 'n':
        break
    else:
        print('Not (Y)es or (N)o')
