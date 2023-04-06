import sys
from operator import add

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

"""
从socket中读数据

执行过程：
  (1)运行 nc -lk 9999
  (2)执行脚本 spark2-submit network_wc.py localhost 9999 >out.log
  (3)out.log 中查看结果
"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: network_wc.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    ssc = StreamingContext(sc,1)

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))

    counts = lines.flatMap(lambda x:x.split(" "))\
        .map(lambda x:(x,1))\
        .reduceByKey(add)

    counts.pprint()

    ssc.start()
    ssc.awaitTermination()