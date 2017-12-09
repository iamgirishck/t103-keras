echo "# t103-keras" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/iamgirishck/t103-keras.git
git push -u origin master

import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

y = tf.multiply(a, b)

with tf.Session() as sess:
    result = sess.run(y, feed_dict={a: 6, b: 7})
    print(result)