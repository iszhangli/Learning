# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 2. 前向传播.py
@time: 2020/02/25 22:05:43
"""

import tensorflow as tf

# out = Relu{Relu{Relu[x@w+b]@w+b}@w+b}

# 输入节点为786，第一层输出节点为256，二层128 三层10

w1 = tf.Variable(tf.random.truncated_normal([784, 256]))
b1 = tf.Variable(tf.zeros([256]))

w2 = tf.Variable(tf.random.truncated_normal([256, 128]))
b2 = tf.Variable(tf.zeros([128]))

w3 = tf.Variable(tf.random.truncated_normal([128, 10]))
b3 = tf.Variable(tf.zeros([10]))

x = tf.random.uniform([128, 28, 28], maxval=256)

x = tf.reshape(x, [-1, 28*28])

h1 = x@w1 + tf.broadcast_to(b1, [x.shape[0], 256])
h1 = tf.nn.relu(h1)

h2 = h1@w2 + b2
h2 = tf.nn.relu(h2)

out = h2@w3 + b3

loss = tf.square(tf.random.uniform([128,10]) - out)
loss = tf.reduce_mean(loss)

print(28*28)
