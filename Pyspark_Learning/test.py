from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from operator import add
from lib.log_handler import LogHandler
logger = LogHandler('test spark')

# spark = SparkSession.builder.master('local[*]').appName('test').enableHiveSupport().getOrCreate()
#
# df = spark.sql('select * from hicon.eva_diag_line_all')
#
# print(df.show())

# 想要访问大数据环境，必须要访问两个文件
# jar包 和 配置文件，如果有服务，开启服务
# 元数据在哪里，在mysql中 mariadb
# 连接地址 用户名 密码 驱动包
# 需要将 hive-site.xml和mysql的驱动包，放在spark-home中，如果配置了metastore服务，还需要开启这个服务


def day01():
    conf = SparkConf().setMaster('local[1]').setAppName('test')
    sc = SparkContext.getOrCreate(conf)
    rdd = sc.textFile(r'E:\Codes\HolidayFlowPredict\conf\flow.csv')
    # rdd = sc.parallelize([1, 2, 3, 4])
    # print(rdd.collect())

    # 查看rdd中每个元素的类型
    # print(rdd.map(lambda x: type(x)).collect())

    rdd = rdd.map(lambda x: float(x[1:-1]))
    # rdd.foreach(lambda x: print('dai wa zi%f' % x))  # foreach 没有返回值，在函数中处理全部的元素
    # print(rdd.getCheckpointFile())
    # print(rdd.getNumPartitions())  # 获取分区数，这个鬼东西有什么用，i have no idea
    # print(rdd.getStorageLevel())
    # print(rdd.glom().collect())  # 将每个分区的数据收集为一个list， 然后返回rdd
    # rdd = rdd.foreachPartition(lambda x: [i for i in x])
    # print(rdd.collect())

def day02():
    conf = SparkConf().setMaster('local[1]').setAppName('test')
    sc = SparkContext.getOrCreate(conf)
    # mapPartitionsWithIndex
    l = ['love1', 'love2', 'love3', 'love4', 'love5', 'love6', 'love7', 'love8', 'love9', 'love10']
    rdd = sc.parallelize(l, 3)
    # print(rdd.getNumPartitions())
    # print(rdd.collect)
    #
    # 继承父类的分区数
    def f(inter, src):
        """也就是说每个分区中的值是一条一条传入的"""
        yield src


    rdd = rdd.mapPartitionsWithIndex(f)
    print(rdd.collect())

def day03():
    # 运行模式
    # local --IDE中,要用local模式，本地模式，多用于测试模式
    # stanalone  -- spark 自带的资源调度框架，支持分布式搭建
    # cluster
    # yarn -- hadoop生态圈中的资源调度
    # mesos
    conf = SparkConf().setMaster('local').setAppName('day_03')
    sc = SparkContext.getOrCreate(conf)
    # spark中一个核的概念是 线程 例如 4核8线程 可以为spark提供8个核
    # 数据加载 是一行一行加载的
    lines = sc.textFile('./../data/word.txt')
    # flat map是一对多的关系
    # f中的输入参数是一行一行的数据，返回是一个集合
    def f(line):  # 证实输入是一行，然后对这一行进行处理，然后拼接成一个[]
        print('i am a %s' % line)
        m = line.split(' ')
        # logger.info(m)
        print("m[0] is %s, m[1] is %s" % (m[0], m[1]))
        return [m[0]] + m[1][:-1].split('.')
        # return line
    words = lines.flatMap(f)
    # 元祖行为称为（k, v）格式的
    k_v = words.map(lambda x: (x,1))
    # 转化为(key, value)格式的数据，一定要想到 *ToPair
    # 1. 先将相同的key分组
    # 2. 对每一组的key对应的value，按照逻辑去处理
    def f1(int1, int2):
        return int1+int2
    num = k_v.reduceByKey(f1)

    # print(num.collect())
    # 排序，传入的是一个个的tuple
    # 也可以使用sortByKey,但是需要将value和key的格式调换
    def f2(value):  # 传入tuple
        return value[1]
    num = num.sortBy(f2, False)
    # words.foreach(print)
    num.foreach(print)  # 打印可迭代的对象

def day04():

    # conf = SparkConf().setMaster('local').setAppName('day_04')
    sc = SparkContext.getOrCreate()

    rdd = sc.parallelize(['a', 'b', 'c', 'd', 'e', 'f'], 1)
    # k v 格式的rdd，如果输出字典格式的rdd，会怎么样呢？

    print(rdd.getNumPartitions())  # 在默认配置的情况下，使用几个分区

    sc.stop()
    sc.close()

def day05():
    sc = SparkContext.getOrCreate()
    # 需要避开字典格式，以后使用元祖形式
    rdd1 = sc.parallelize([('eva', 10), ('evan', 20), ('ryan', 30), ('queen', 30)], 3)
    rdd2 = sc.parallelize([('eva', 100), ('evan', 200), ('ryan', 300), ('eva', 112)], 2)
    # 将相同key的value聚合， 是一个shuffer的操作
    # 只有相同的key才能聚合到一起，
    # 与父rdd多个那个分区数保持一致[java]？？ 分区数也是两个父分区相加[python]
    join = rdd1.join(rdd2)
    print(rdd1.getNumPartitions())

    # 以左为主
    left_join = rdd1.leftOuterJoin(rdd2,1)
    # print(left_join.collect())
    # rightOuterJoin

    # fullOuterJoin
    full_join = rdd1.fullOuterJoin(rdd2)
    # print(full_join.collect())

    # union
    # 合并rdd, 类型必须一样，只是逻辑上的合并
    # 分区是两个父partitions相加
    rdd = rdd1.union(rdd2)

    rdd = rdd1.intersection(rdd2)

    # rdd1比rdd2差在哪里？
    rdd = rdd1.subtract(rdd2)

    rdd = rdd1.cogroup(rdd2)
    print(rdd.getNumPartitions())
    print(rdd.collect())

def day06():
    sc = SparkContext.getOrCreate()
    l = ['love1', 'love2', 'love3', 'love4', 'love5', 'love6', 'love7', 'love8', 'love9', 'love10']
    rdd = sc.parallelize(l, 3)
    def f1(ele):
        print('create connect database')
        print('insert data %s' % ele)
        return ele + '_yes'
    rdd1 = rdd.map(f1)

    # mapPartitions()
    # 分区的数据一次性读进来
    # mapPartitions完全可以取代map，因为mapPartitions拥有很高的性能
    def f2(ele):
        print('create connect database')
        l = []
        for i in ele:  # 作为迭代器，迭代完之后就啥也没有了
            print('insert data %s' % i)
            l.append(i)
        return l
    rdd2 = rdd.mapPartitions(f2)

    # foreach 是一个action算子
    # foreachPartitions()

    # 去重实例
    l = ['a', 'b', 'c', 'a']
    rdd = sc.parallelize(l, 1)
    map_rdd = rdd.map(lambda x: (x,1))
    reduce_rdd = map_rdd.reduceByKey(add)
    result = reduce_rdd.map(lambda x: x[0])
    print(result.collect())

def day07():
    conf = SparkConf().setMaster('local[1]').setAppName('test')
    sc = SparkContext.getOrCreate(conf)
    # mapPartitionsWithIndex
    l = ['love1', 'love2', 'love3', 'love4', 'love5', 'love6', 'love7', 'love8', 'love9', 'love10']
    rdd = sc.parallelize(l, 3)
    #
    # 会将索引下标带出来，可能会有用吧
    # 和mapPartitions的区别在哪里
    def f1(index, ele):
        print('index is %d, ele is %s' % (index, [i for i in ele]))
        return ele
    i = rdd.mapPartitionsWithIndex(f1)
    print(i.collect())
    # rePartitions()
    # 重新分区
    re_i = rdd.repartition(1)
    i = re_i.mapPartitionsWithIndex(f1)

    # coalesce
    # 与repartition一样，可以增多分区，也可以减少分区
    # 可以指定是否 shuffle
    co_i = rdd.coalesce(1)
    i = co_i.mapPartitionsWithIndex(f1)
    print(i.collect())

def day08():
    conf = SparkConf().setMaster('local[1]').setAppName('test')
    sc = SparkContext.getOrCreate(conf)
    l = [('ryan', 12), ('ryan', 12), ('ryan', 12), ('ryan', 12), ('eva', 10), ('eva', 10), ('eva', 10), ('eva', 10), ('eva', 10), ('eva', 10)]
    rdd = sc.parallelize(l)
    rdd1 = sc.parallelize(l)

    # groupByKey()
    # 将相同的key聚合在一起
    group = rdd.groupByKey()
    zip = rdd.zip(rdd1)

    # 给rdd的每个元素压缩成一个key value格式的数据
    zip_index = rdd.zipWithIndex()
    # print(group.collect())
    def f1(i):
        for k in i[1]:
            print(k)
    # zip_index.foreach(print)

    # reduce
    def f2(v1, v2):
        # 也可以算，只不过需要再函数中拼接更多的数值
        if type(v1) is list:
            # print('i am not list, print v1 % ' % v1)
            l = v1
        else:
            print(type(v1))
            l = [v1]
        print('1 is %s' % l)
        l.append(v2)
        print('2 is %s' % l)

        return l

    # re = rdd.reduce(f2)

    k = rdd.countByKey()
    v = rdd.countByValue()
    print(v.items())

if __name__ == '__main__':
    day08()
