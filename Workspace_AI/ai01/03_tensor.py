import tensorflow as tf

#  tf.placeholder : 그래프를 실행 시 데이터 입력!
node1 = tf.placeholder(dtype=tf.float32)
node2 = tf.placeholder(dtype=tf.float32)
node3 = node1 + node2

sess = tf.Session()

print(sess.run(node3, feed_dict={node1:[10, 20, 30], node2:[40, 50, 60]}))



