import tensorflow as tf

# 1. training data set (학습 데이터셋)
x = tf.placeholder(tf.float32)

# label (정답)
y = tf.placeholder(tf.float32)

# 2. Weight & bias를 정의
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# 3. Hypothesis 가설 설정
H = W * x + b

# 4. loss function
# 가설에서 정답을 빼서 제곱한 값들을 모두 더해서 평균을 낸 그래프
loss = tf.reduce_mean(tf.square(H - y))

# 5. gradient decent algorithm (경사하강법)
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# 6. 실행 준비
sess = tf.Session()

# 초기화
sess.run(tf.global_variables_initializer())

# 7. 학습
epochs = 3000

for step in range(epochs):
    tmp, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={x: [1, 2, 3, 4 ,5], y: [1, 2, 3, 4, 5]})
    if step % 300 == 0:
        print(f'Weight: {W_val} \t bias: {b_val} \t loss: {loss_val}')

# 8. prediction 예측
print(sess.run(H, feed_dict={x: [10, 20, 30, 40, 50]}))