# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 8. rdd_dateframe.py
@time: 2020/02/15 18:09:30
"""

from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.master('local[*]').appName('rdd_to_dataFrame').getOrCreate()

# RDD的互操作性
# RDD 转成 dataframe
# 第一种方法：基于RDD的反射机制转换成dataframe
sc = spark.sparkContext
rdd = sc.textFile(r'./age_name.txt')

result = rdd.map(lambda line: line.split(',')).map(lambda arr: (arr[0], int(arr[1])))
print(result.collect())

df = result.toDF(('A', 'B'))
print(df.show())
df = result.toDF(['name', 'age'])
print(df.show())

# 第二种，直接给定schema信息
# dataFrame中的数据结构信息，即为schema信息
result1 = rdd.map(lambda line: line.split(','))
people = result1.map(lambda arr: Row(xiaohuozi=arr[0], age=int(arr[1])))
df2 = spark.createDataFrame(people)
print(df2.show())

