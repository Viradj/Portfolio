from __future__ import print_function
import tensorflow as tf

# import data
	from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/train-images.idx3-ubyte", one_hot=True) #one_hot betekend formation data for computers (beter machine readeble)

#hyperparameters
learing_rate = 0.001 # weight opdating thing 1e-3
training_iters = 200000
batch_size = 128 #hoeveel sample (wat we trainen) | de beste is 64
display_step = 10 #hoevaak willen we de leerstappen laten zien?

#network parameters
n_input = 784 # 28 x 28 pixel image
n_classes = 10 # aantal classes omdat er 10 mogelijke cijfers (classes) zijn in de dataset
dropout = 0.75 # het zorgt ervoor dat nuronen tijdens het traien worden sommige neronen worden uitgeschakkeld zodat er wordt geforceerd andere manieren te vinden om tot het antwoord te komen. 

x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32)

def conv2d(x, W, b, strides=1):
# confolustion is a fancy word for stransform 
	x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1]), padding = 'SAME'
	x = tf.nn.bias_add(x, b)
	return tf.nn.relu(x) 

def maxpool2d(x, k=2):
	return tf.nn.max_pool(x, ksize=[1,k,k,1], strides=[1,k,k,1], padding= 'SAME')

#Creat model
def conv_net(x, weight, biases, dropout):
	x = tf.reshape(x, shape=[-1, 28, 28, 1])

	#convoutional layer
	conv1 = conv2d(x, weight['wc1'], biases['bc1'])
	#max pooling
	conv1 = maxpool2d(conv1, weights[ 'wc2'], biases['bc2'])
	#what the hell is maxpooling layers???
	conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
	conv2 = maxpool2d(conv2,k=2)

	fc1 = tf.reshape(conv2, [ -1, weights['wd1'].get_shape().as_list()]) # mogelijk moet deze ]) aan het einden weg maar ik ben niet zeker. 
	fc1 = tf.add(tf.matmul(fc1, weights['wd1'], biases['bd1'])) #matrix mulification
	fc1 = tf.nn.relu(fc1)

	# toevoegen dropoup
	fc1 = tf.nn.dropout(fc1, dropout)

	# output, class, predition
	out = tf.add(tf.matmul(fc1, weights['out'], biases['out']))
		return out

# Aanmaken weights
weights = {
	'wc1': tf.Variable(tf.random_normal([5,5,1,32])),
	'wc2': tf.Variable(tf.random_normal([5,5,32,64])),
	'wc1': tf.Variable(tf.random_normal([7*7*64, 1024])),
	'out': tf.Variable(tf.random_normal(1024, n_classes))
}

# construct model
pred = conv_net(x, weights, biases, keep_prob)

cost = tf.reduce_mean(tf.nn.soft_cross_entropy_with_logits(pred, y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# evaluatie model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.initialize_all_variables()


with tf.Session() as sess:
    sess.run(init)
    step = 1
    # Keep training until reach max iterations
    while step * batch_size < training_iters:
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        # Run optimization op (backprop)
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y,
                                       keep_prob: dropout})
        if step % display_step == 0:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([cost, accuracy], feed_dict={x: batch_x,
                                                              y: batch_y,
                                                              keep_prob: 1.})
            print("Iter " + str(step*batch_size) + ", Minibatch Loss= " + \
                  "{:.6f}".format(loss) + ", Training Accuracy= " + \
                  "{:.5f}".format(acc))
        step += 1
    print("Optimization Finished!")

    # Calculate accuracy for 256 mnist test images
    print("Testing Accuracy:", \
        sess.run(accuracy, feed_dict={x: mnist.test.images[:256],
                                      y: mnist.test.labels[:256],
                                      keep_prob: 1.}))