# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: helloworld.py
@time: 2020/02/06 21:33:45
"""

from pyspark import SparkConf, SparkContext
import os

if 'Spark_Home' not in os.environ:
    os.environ['Spark_Home'] = ''

# 构建上下文
conf = SparkConf().setMaster('local[*]').setAppName('wordcount')

sc = SparkContext.getOrCreate(conf)

"""
初始化RDD的方法
"""
# 读取数据形成RDD, 这是读取内存中的数据形成的RDD

l = [1, 2, 3, 4, 5]
rdd = sc.parallelize(l)

print(rdd.collect())

# 查看分区
# print(rdd.getNumPartitions())  # 电脑的核数
# 按照分区打印数据
# print(rdd.repartition(5).glom().collect())
# [[], [], [2, 3], [1], [4, 5]]
# 分区根据hash

# 读取外部文件系统的文件，形成RDD
# 读取本地文件，形成RDD
path = r'E:\Codes\PythonWorkspace\Pyspark\README.md'
rdd = sc.textFile(path)
print(rdd.collect())

# 读取hdfs文件形成RDD
# path = r'' # hdfs的文件系统
rdd = sc.textFile(path)
print(rdd.collect())

# 读取所有一个文件下的所有文件
path = './'
rdd = sc.wholeTextFiles(path)
print(rdd.take(2))
