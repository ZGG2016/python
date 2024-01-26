import sys
import unittest
from test_list import TestListMethodsCase
from test_string import TestStringMethodsCase

# 使用测试套件
# 把测试用例和测试套件放在与被测试代码相同的模块中，但将测试代码放在单独的模块中
if __name__ == '__main__':
    # result = unittest.TestResult(sys.stdout, 'test result', 1)
    suite = unittest.TestSuite()
    # 1.1 加载测试用例方法
    # suite.addTest(TestStringMethodsCase("test_upper"))  # 测试类(测试方法)
    # suite.addTests([TestStringMethodsCase("test_upper"), TestStringMethodsCase("test_isupper")])

    # 1.2 加载测试用例类
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestListMethodsCase))
    suite.addTest(loader.loadTestsFromTestCase(TestStringMethodsCase))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print("result.testsRun ==> ", result.testsRun)

    # 1.3 加载指定路径里的测试用例
    # test_dir = "F:\\CODE\\python\\code\\pythoncode\\basic\\website\\Python 标准库\\unittest"
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern="*_string.py")
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

