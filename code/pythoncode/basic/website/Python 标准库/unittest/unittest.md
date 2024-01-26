
[https://docs.python.org/zh-cn/3.8/library/unittest.html](https://docs.python.org/zh-cn/3.8/library/unittest.html)

命令行下

```sh
PS F:\CODE\python\code\pythoncode\basic\website\Python 标准库\unittest> python -m unittest -v test_string.TestStringMethods
test_isupper (teststringmethods.TestStringMethods) ... ok
test_split (teststringmethods.TestStringMethods) ... ok
test_upper (teststringmethods.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
PS F:\CODE\python\code\pythoncode\basic\website\Python 标准库\unittest> python -m unittest -v test_string.TestStringMethods.test_upper
test_upper (teststringmethods.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

- -f 出现第一个错误或失败时，停止运行测试

```sh
PS F:\CODE\python\code\pythoncode\basic\website\Python 标准库\unittest> python -m unittest -v test_string.TestStringMethods.test_upper -f
test_upper (test_string.TestStringMethods) ... FAIL

======================================================================
FAIL: test_upper (test_string.TestStringMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "F:\CODE\python\code\pythoncode\basic\website\Python 标准库\unittest\test_string.py", line 7, in test_upper
    self.assertEqual('Foo'.upper(), 'Foo')
AssertionError: 'FOO' != 'Foo'
- FOO
+ Foo


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

- -k 只运行匹配上的测试方法和类

```shell
PS F:\CODE\python\code\pythoncode\basic\website\Python 标准库\unittest> python -m unittest -v -k list
test_append (test_list.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

PS F:\CODE\python\code\pythoncode\basic\website\Python 标准库\unittest> python -m unittest -v -k upper
test_isupper (test_string.TestStringMethods) ... ok
test_upper (test_string.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
- -s 开始进行搜索的目录
- -p 指定匹配的模式

```shell
PS F:\CODE\python\code\pythoncode\basic\website\Python 标准库> python -m unittest discover -v -s .\unittest\ -p 'test_*.py'
test_append (test_list.TestStringMethods) ... ok
test_isupper (test_string.TestStringMethods) ... ok
test_split (test_string.TestStringMethods) ... ok
test_upper (test_string.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
