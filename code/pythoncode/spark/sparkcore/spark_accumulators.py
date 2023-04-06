import sys

from pyspark.accumulators import AccumulatorParam
from pyspark.context import SparkContext

# spark2 自定义累加器

class SparkCounter(AccumulatorParam):
    def zero(self, value):
        return value

    def addInPlace(self, value1, value2):
        for key, value in value2.items():
            if key in value1:
                value1[key] += value
            else:
                value1[key] = value
        return value1

def update_counter(counter, path):
    if isinstance(counter, dict):
        counter[path] += 1
    else:
        counter.add({path: 1})

def main():
    sc = SparkContext()
    g_counter = sc.accumulator({"a": 1, "b": 1}, SparkCounter())

    for i in range(0,10):
        if i%2==0:
            update_counter(g_counter, "a")
        else:
            update_counter(g_counter, "b")

    print(g_counter.value)


if __name__=="__main__":
    """"   
     standalone 集群运行：
        spark2-submit spark_accumulators.py --master spark2://zgg:7077
     本地运行：
        spark2-submit spark_accumulators.py --master local 
    
     结果：{'a': 6, 'b': 6}
    """
    main()


"""
AccumulatorParam 自定义一个累加器要继承的类

>>> from pyspark.accumulators import AccumulatorParam
>>> class VectorAccumulatorParam(AccumulatorParam):
...     def zero(self, value):
...         return [0.0] * len(value)
...     def addInPlace(self, val1, val2):
...         for i in range(len(val1)):
...              val1[i] += val2[i]
...         return val1
>>> va = sc.accumulator([1.0, 2.0, 3.0], VectorAccumulatorParam())
>>> va.value
[1.0, 2.0, 3.0]
>>> rdd = sc.parallelize([1,2,3])
>>> def g(x):
...     global va
...     va += [x] * 3
>>> rdd.foreach(g)
>>> va.value
[7.0, 8.0, 9.0]
"""