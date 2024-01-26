import sys
import unittest
import HtmlTestRunner

if __name__ == '__main__':

    test_dir = "F:\\CODE\\python\\code\\pythoncode\\basic\\website\\Python 标准库\\unittest"

    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")

    runner = HtmlTestRunner.HTMLTestRunner(output="./reports/",
                                           stream=sys.stderr,
                                           report_name="自动化测试报告",
                                           report_title="TEST RESULTS ==> ",
                                           )
    runner.run(discover)
