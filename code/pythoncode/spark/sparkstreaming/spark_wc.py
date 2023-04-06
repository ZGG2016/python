import sys
from operator import add
from pyspark import SparkContext, SparkConf

# spark2 wordcount

def main(flag):
    global data
    conf = SparkConf().setMaster("local").setAppName("wordcount")
    sc = SparkContext(conf=conf)

    # resource = sc.parallelize(["a,b","b,c"])

    # 从hdfs读取文件  hdfs://localhost:9000/user/hadoop/word.txt
    if flag=='0':
        data = sc.textFile("hdfs://zgg:9000/in/datasource.txt")
        #resource = sc.textFile("/in/datasource.txt")

    # 从本地读取文件 --- 绝对路径
    elif flag=='1':
        data = sc.textFile("file:///root/resource/datasource.txt")

    rdd = data.flatMap(lambda x:x.split(" ")).map(lambda x:(x,1)).reduceByKey(add)

    rlt = rdd.collect()
    for (word,count) in rlt:
        print(word,count)

    sc.stop()

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("input params,please")

    """"
     0：从hdfs读
     1：从本地读
    """

    flag = sys.argv[1]
    main(flag)

"""
standalone 集群运行：
spark2-submit spark_wc.py --master spark2://zgg:7077 [flag]

---------------------------------------------

系统默认是从hdfs://localhost:9000/目录下读取文件的，但是README.md文件在本地目录下，
并不在这一目录下，所以sc.textFile()必须使用绝对路径。
"""




