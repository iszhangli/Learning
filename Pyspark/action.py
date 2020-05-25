# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: action.py
@time: 2020/02/11 20:55:27
"""

from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster('local[*]').setAppName('TransFormation')
sc = SparkContext.getOrCreate(conf)

#
rdd1 = sc.parallelize([1, 2, 3])
rdd2 = sc.parallelize([2, 3, 4])
# 并集
unionRDD = rdd1.union(rdd2)
print(unionRDD.collect())

# 交集
intersectionRDD = rdd1.intersection(rdd2)
print(intersectionRDD.collect())

# 差集
subtractRDD = rdd1.subtract(rdd2)
print(subtractRDD.collect())

# 笛卡尔积
cartesianRDD = rdd1.cartesion(rdd2)
print(cartesianRDD.collect())

# join

