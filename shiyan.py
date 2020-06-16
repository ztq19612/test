import tensorflow as tf
a = [0,1,1,0,0,0,1,0,1,1]
b = tf.one_hot(a,2,dtype=tf.int32)
print(type(b))
def onehot_labels(b):
    b = b.numpy()
    c = []
    for i in range(b.shape[0]):
        if b[i,1] == 1:
            c.append(1)
        else:
            c.append(0)
    print(type(c))
    print(c)
    return c
print(tf.argmax(b, 1))
onehot_labels(b)
gamma = 5
y_pred = tf.reshape([[1.,2.],[1.,3.]],[2,2])
y_true = [0,1]
softmax = tf.reshape(tf.nn.softmax(y_pred), [-1])

labels = tf.range(0, y_pred.shape[0]) * y_pred.shape[1] + y_true
print(labels)
prob = tf.gather(softmax, labels)
print(softmax)
print(prob)
weight = tf.pow(tf.subtract(1., prob), gamma)

loss = -tf.reduce_mean(tf.multiply(weight, tf.math.log(prob)))
print(loss)
def focal_loss_calc(alpha=0.25, gamma=2., epsilon=1e-6):
    """ focal loss used for train positive/negative samples rate out
    of balance, improve train performance
    """
    def focal_loss(y_true, y_pred):
        positive = tf.where(tf.equal(y_true, 1), y_pred, tf.ones_like(y_pred))
        negative = tf.where(tf.equal(y_true, 0), y_pred, tf.zeros_like(y_pred))
        return -alpha*K.pow(1.-positive, gamma)*K.log(positive+epsilon) - \
            (1-alpha)*K.pow(negative, gamma)*K.log(1.-negative+epsilon)
    return focal_loss