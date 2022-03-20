import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    x_train,
    y_train,
    epochs=100,
    batch_size=256,
    validation_data=(x_test, y_test),
    validation_freq=1
)
