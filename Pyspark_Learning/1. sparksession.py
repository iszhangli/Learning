
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

#
spark = SparkSession.builder.\
    master('local[*]').\
    appName('learning').\
    config(conf=SparkConf()).\
    getOrCreate()  # 可以获取一个现有的，如果不存在，可以获取一个新的




