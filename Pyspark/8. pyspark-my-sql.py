# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 8. pyspark-my-sql.py
@time: 2020/03/16 21:50:05
"""

from pyspark.sql import SparkSession
import os

# 我要关注的点是 怎么从数据库读取数据
# 怎么将数据写入数据库

# 1. 构建上下文
spark = SparkSession.builder.master('local[*]').appName('pyspark sql')
df -

