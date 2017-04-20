import numpy as np
import pickle
import tensorflow as tf
'''
array_loaded = np.load('bvlc_alexnet.npy')
for i,j in enumerate(array_loaded[()]):
	print i,j

#np.savetxt('conv.txt',array_loaded[()][u'conv1'],delimiter=',',fmt='%.18e')

#new_array = array_loaded[()][u'conv1']
print len(array_loaded[()][u'conv1'][1])

with open('weights.txt','rw+') as f:
	f.write(new_array)
'''
matrix = np.arange(16.0).reshape((2,2,2,2))

a = tf.Variable(matrix)
init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)
	b = a.get_shape().as_list()
	c = a.eval(sess)
print('main array = ')
print(c)
down = 1
for i in b:
	down = down*i
c = np.reshape(c,down)	
print '\nflattened array = '+`c`
for i in range(len(c)):
	if c[i]%2==0:
		c[i]=float('NaN')

for j in range(len(c)):
	c[j] *= 2
	
d = np.reshape(c,b)
print('\ntransformed array = ')
print(d)
with tf.Session() as sess:
	sess.run(init)
	sess.run(a.assign(d))
	print('new tensor = ')
	print(sess.run(a))