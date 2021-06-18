import tensorflow as tf

# tf.float32 == np.float32 -> tf 내부적으로 numpy 사용
node1 = tf.constant(10, dtype=tf.float32)
node2 = tf.constant(20, dtype=tf.float32)

node3 = node1 + node2
sess = tf.Session()

print(sess.run(node3))

