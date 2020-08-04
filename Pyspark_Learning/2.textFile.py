# Create time: 2020/5/28 14:22
# Author: zhang li

from pyspark import SparkContext

sc = SparkContext.getOrCreate()

rdd = sc.textFile('hdfs://10.16.3.34:8020/user/spark/applicationHistory/')
rdd.collect()
