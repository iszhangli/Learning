# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 7. SparkSQL.py
@time: 2020/02/15 16:34:55
"""

from pyspark.sql import SparkSession

# 1. 构建上下文
spark = SparkSession.builder.master('local[*]').appName('spark_sql').getOrCreate()

# 2. 读取数据形成DataFrame
# 读取json数据, 需要的json格式为一行
df = spark.read.json(r'./country.json')
print(df.show())

# DSL语法的使用
print(df.printSchema())  # schema信息结构
print(df.select('id').show())
print(df.select(df['cname']).alias('cname').show())  # alias 别名
print(df.agg({'id':'avg'}))
df.groupBy(df['id'])
# df.filter()

# 创建一张临时表
df.createTempView('people')  # 将df注册为一张临时的表
print(spark.sql('select * from people').show())
df.createOrReplaceTempView('people')

# 全局临时视图
# 当前会话中，为局部变量

df.createGlobalTempView('people2')

# print(spark.sql('select * from people2').show())
# pyspark.sql.utils.AnalysisException:
# 'Table or view not found: people2; line 1 pos 14'
# 因为全局临时视图默认存放在 global_temp 数据库中，所以需要指定数据库名称
print(spark.sql('select * from global_temp.people2').show())

# spark_t = spark.newSession()
# spark_t.sql('select * from global_temp.people2')  # 正常运行
# spark_t.sql('select * from people')  # 将报错

# RDD的互操作性
# RDD 转成 dataframe
# 第一种方法：基于RDD的反射机制转换成dataframe
sc = spark.sparkContext
rdd = sc.textFile(r'./age_name.txt')

result = rdd.map(lambda line: line.split(','))\
    .map(lambda arr: (arr[0], int(arr[1])))
print(result.collect())

rdd_to_df = rdd.toDF(['name', 'age'])  # rdd到df
print(rdd_to_df.show())

# 第二种方法 的 第一种：直接给定schema信息
from pyspark.sql import Row
result1 = rdd.map(lambda line: line.split(','))
people = result1.map(lambda arr: Row(name=arr[0], age=arr[1]))
df2 = spark.createDataFrame(people)
print(df2.show())

# 第二种方法的 第二种 直接给定schema信息


spark.udf.register()

class MyAvg():
    def __init__(self):
        pass
    def len(self):
        return 1
spark.udf.registerJavaUDAF('udaf', MyAvg)






