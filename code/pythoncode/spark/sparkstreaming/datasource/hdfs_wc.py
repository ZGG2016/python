import sys
from operator import add

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

"""
从hdfs中读数据

执行过程：
  (1)运行脚本 spark2-submit hdfs_wc.py /in/streaming/ >out.log 
  (2)在 /in/streaming/ 目录下，创建新文件，然后就可以对新增的文件进行计数了
  (3)out.log 中查看结果
"""

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: hdfs_wordcount.py <directory>",file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingHDFSWordCount")
    ssc = StreamingContext(sc,1)

    lines = ssc.textFileStream(sys.argv[1])

    counts = lines.flatMap(lambda x:x.split(" ")).map(lambda x:(x,1)).reduceByKey(add)

    counts.pprint()

    ssc.start()
    ssc.awaitTermination()