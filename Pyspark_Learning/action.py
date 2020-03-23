# !/usr/bin/env python
# -*- coding:utf-8 -*-
# name: action 
# author: li zhang
# date: 2020/2/12

from pyspark import SparkConf, SparkContext

# jdbc java版的ODBC，开放的数据库连接，一套公共的接口，用来连接数据库
#

# action

# saveAsTextFile() 封装好的方法


# saveAsTextFile()

conf = SparkConf().setAppName('test').setMaster('local[*]')
sc = SparkContext().getOrCreate(conf)

rdd = sc.parallelize([1,2,3,4,5])
print(rdd.collect())