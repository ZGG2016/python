import unittest


class Widget:
    def __init__(self, name):
        self.name = name
        self.lst = []

    def size(self):
        return len(self.lst)

    def resize(self):
        self.lst.append('a')
        return len(self.lst)

    def dispose(self):
        self.lst.clear()


class WidgetTestCase(unittest.TestCase):
    # 在调用测试方法前调用
    def setUp(self):
        print("setUp....")
        self.widget = Widget("The widget")

    def test_default_widget_size(self):
        # 测试未通过，显示的字符串
        self.assertEqual(self.widget.size(), 0, 'wrong default size')

    def test_widget_resize(self):
        self.widget.resize()
        self.assertEqual(self.widget.size(), 1, 'wrong size after resize')
        # self.assertEqual(self.widget.size(), 2, 'wrong size after resize')

    # 在测试方法被调用并记录结果之后立即被调用的方法。 此方法即使在测试方法引发异常时仍会被调用
    # 此方法将只在 setUp() 成功执行时被调用，无论测试方法的结果如何
    def tearDown(self):
        print("tearDown....")
        self.widget.dispose()


if __name__ == '__main__':
    unittest.main()
