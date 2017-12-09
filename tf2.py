# example-1-basic.py
import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multiply(a, b)

with tf.Session() as sess:
    result = sess.run(y, feed_dict={a: 6, b: 7})
    print(result)