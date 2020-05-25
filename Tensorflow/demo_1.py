# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: demo_1.py
@time: 2020/02/25 21:51:29
"""

import tensorflow as tf

a = tf.constant(1,2)
a = tf.range(5)
b = tf.constant(2)

print(a)

a = tf.random.normal([3,4,32,2])
b = tf.random.normal([3,4,2,1])
print(a@b)

