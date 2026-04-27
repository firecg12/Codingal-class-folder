#i fixed the error when installing packages(tensorflow) by using py 10
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
# Load MNIST dataset


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# Normalize the pixel values
x_train, x_test = x_train / 255.0, x_test / 255.0
# Build the neural network model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Make predictions
predictions = model.predict(x_test)

# Display the first image and its predicted label
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.xlabel(f'Predicted: {predictions[0].argmax()}')
plt.show()
