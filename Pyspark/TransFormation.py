# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: TransFormation.py
@time: 2020/02/10 20:41:46
"""

from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster('local[*]').setAppName('TransFormation')
sc = SparkContext.getOrCreate(conf)

# RDD提供的一系列转换算法
# map flatmap filter distinct sample sortBy
numberRDD = sc.parallelize(range(1, 11))
print(numberRDD.collect())


mapRDD = numberRDD.map(lambda x: x**2)
# print(mapRDD.collect())

# 如果时数组的形式，使用flatMap， 这里也这是单个元素，没有再改
flatMapRDD = numberRDD.flatMap(lambda x: (x, x**2, x**3))
# print(flatMapRDD.collect())

# 过滤
filterRDD = numberRDD.filter(lambda x: x % 3 == 0)
# print(filterRDD.collect())

# sample 抽样
sampleRDD = numberRDD.sample(False, 0.5, 81)
# print(sampleRDD.collect())

# 排序
sortRDD = flatMapRDD.sortBy(lambda x: x)
# print(sortRDD.collect())

# distinct 去重

# PairByKey 提供的算子
# groupByKey reduceByKey sortByKey aggregateByKey sampleByKey
rdd = sc.parallelize(["Hello hello", "Hello New York", "Hi Beijing"])
pairRDD = rdd.flatMap(lambda x: x.split(' '))\
    .map(lambda word: word.lower())\
    .map(lambda word: (word, 1))
print(pairRDD.collect())

