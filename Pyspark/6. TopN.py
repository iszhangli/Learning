# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 6. TopN.py
@time: 2020/02/15 13:51:16
"""
from pyspark import SparkContext, SparkConf
import random

conf = SparkConf().setMaster('local[*]').setAppName('topN')

sc = SparkContext.getOrCreate(conf)

rdd = sc.textFile(r'./en.txt')

result = rdd.flatMap(lambda line: line.split(' ')).map(lambda x: (x, 1))\
    .filter(lambda arr: len(arr) == 2)\
    .mapPartitions(lambda iter: map(lambda arr: ((random.randint(1,10), arr[0]), arr[1]), iter))\
    .groupByKey().flatMap().groupByKey().map()

print(result.collect())