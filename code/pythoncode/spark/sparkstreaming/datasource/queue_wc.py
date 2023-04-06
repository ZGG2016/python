import time
from operator import add

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
"""
 Create a queue of RDDs that will be mapped/reduced one at a time in
 1 second intervals.

 To run this example use
    `$ spark2-submit queue_stream.py >out.log
"""
if __name__=="__main__":

    sc = SparkContext(appName="PythonStreamingQueueStream")
    ssc = StreamingContext(sc,1)

    rddqueue = []
    for i in range(5):
        rddqueue += [ssc.sparkContext.parallelize([j for j in range(1,1001)],10)]

    lines = ssc.queueStream(rddqueue)
    counts = lines.map(lambda x: (x % 10, 1)).reduceByKey(add)

    counts.pprint()

    ssc.start()
    time.sleep(6)
    ssc.stop(stopSparkContext=True, stopGraceFully=True)