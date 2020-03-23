# !/usr/bin/env python
# -*- coding:utf-8 -*-
# name: demo_1 
# author: li zhang
# date: 2020/2/25

import tensorflow as tf
from tensorflow.keras import layers

a = tf.constant([2,3])
print(a)


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=10000)



