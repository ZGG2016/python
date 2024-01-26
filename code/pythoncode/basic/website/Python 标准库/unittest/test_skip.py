import sys
import unittest

import pandas
from test_widget import Widget


def external_resource_available():
    return False


# 自定义的跳过测试装饰器
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


# 跳过测试方法
class SkipTestCase(unittest.TestCase):

    # TestCase.setUp() 也可以跳过测试。可以用于所需资源不可用的情况下跳过接下来的测试
    # @unittest.skipIf(not external_resource_available(), "skiping setUp")
    # def setUp(self):
    #     pass

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(pandas.__version__ == '1.3.0',
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass

    # @skipUnlessHasattr(Widget("The widget"), 'lst')
    @skipUnlessHasattr(Widget("The widget"), 'aaa')
    def test_custom_skip(self):
        print("test_custom_skip.....")


# 跳过测试类
# @unittest.skip("showing class skipping")
# class MySkippedTestCase(unittest.TestCase):
#     def test_not_run(self):
#         pass


if __name__ == '__main__':
    unittest.main()

# 被跳过的测试的 setUp() 和 tearDown() 不会被运行。
# 被跳过的类的 setUpClass() 和 tearDownClass() 不会被运行。
# 被跳过的模组的 setUpModule() 和 tearDownModule() 不会被运行。
