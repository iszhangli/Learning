# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 5.词频统计.py
@time: 2020/02/15 09:23:30
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local[*]').setAppName('word count')
sc = SparkContext.getOrCreate(conf)

rdd = sc.textFile(r'./en.txt')

# flatMap 展开后是一维list
wd = rdd.flatMap(lambda line: line.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x+y)

print(wd.top(3, lambda x: x[1]))

print(wd.collect())