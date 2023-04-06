from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("checkpoint")
sc = SparkContext(conf=conf)

sc.setCheckpointDir("hdfs://zgg:9000/spark2/checkpoint")

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9],2)
res = rdd.map(lambda x:x+1).cache()
res.checkpoint()

print(res.count())

"""
standalone 集群运行：
spark2-submit checkpoint.py --master spark2://zgg:7077
"""