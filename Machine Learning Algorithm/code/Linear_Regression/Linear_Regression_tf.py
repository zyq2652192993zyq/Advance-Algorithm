import tensorflow as tf
from tensorflow import data
from tensorflow import keras
from tensorflow import losses
from tensorflow.keras import optimizers
from tensorflow.keras import layers
from tensorflow import initializers as init

config = {
    "feature_num": 2,
    "sample_num": 1000,
    "batch_size": 10,
    "num_epochs": 3
}


def get_dataset():
    true_w = tf.reshape(tf.constant([2.0, -3.4]), (2, 1))
    true_b = tf.constant([4.2])
    features = tf.random.normal((config['sample_num'], config['feature_num']), stddev=1)
    labels = tf.matmul(features, true_w) + true_b + tf.random.normal((config['sample_num'], 1), stddev=0.01)
    dataset = data.Dataset.from_tensor_slices((features, labels)) \
        .shuffle(buffer_size=config['sample_num']).batch(config['batch_size'])

    return dataset, features, labels, true_w, true_b


def get_model():
    model = keras.Sequential(
        layers.Dense(1, kernel_initializer=init.RandomNormal(stddev=0.01))
    )
    return model


def get_loss():
    return losses.MeanSquaredError()


def get_optimizer():
    return optimizers.SGD(learning_rate=0.03)


def train(dataset, features, labels, model, optimizer, loss):
    for epoch in range(1, config['num_epochs'] + 1):
        for (batch, (X, y)) in enumerate(dataset):
            with tf.GradientTape() as tape:
                l = loss(model(X, training=True), y)

            grads = tape.gradient(l, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))
        l = loss(model(features), labels)
        print(f'epoch {epoch}, loss: {l}')


def main():
    dataset, features, labels, true_w, true_b = get_dataset()
    model = get_model()
    train(
        dataset=dataset,
        features=features,
        labels=labels,
        model=model,
        optimizer=get_optimizer(),
        loss=get_loss()
    )

    print(true_w, model.get_weights()[0])
    print(true_b, model.get_weights()[1])


if __name__ == '__main__':
    main()
