# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: keras.py
@time: 2020/02/26 22:00:21
"""

import tensorflow as tf
from tensorflow import keras

x = tf.constant([2., 1., 0.1])
layer = keras.layers.Softmax(axis=-1)  # 创建softmax层
out = layer(x)  # 前向传播

print(out)

out1 = tf.nn.softmax(x)
print(out1)

