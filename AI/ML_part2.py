import tensorflow as tf

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') > 0.9):
            print("\nReach 90% accuracy so cancelling training!")
            self.model.stop_training = True


mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# plt.imshow(training_images[0])

training_images  = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])
callbacks = myCallback()
model.fit(training_images, training_labels, callbacks=[callbacks])

# model.evaluate(test_images, test_labels)
# classifications = model.predict(test_images)
# print(classifications[0])
# print(test_labels[0])