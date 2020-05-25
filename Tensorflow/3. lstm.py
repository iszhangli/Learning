# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 3. lstm.py
@time: 2020/02/25 22:38:37
"""

import tensorflow as tf

# 拼接和堆叠
# 拼接不会产生新的维度
# 堆叠会产生新的维度
a = tf.random.normal([4,35,8])
b = tf.random.normal([6,35,8])
c = tf.concat([a, b], axis=0)
print(c)