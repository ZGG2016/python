import sys
import unittest


class TestListMethodsCase(unittest.TestCase):
    # 在一个单独类中的测试运行之前被调用的类方法
    @classmethod
    def setUpClass(cls):
        print("TestListMethodsCase setUpClass....")

    def test_append(self):
        lst = ['a', 'b']
        self.assertListEqual(lst, ['a', 'b'])

    # 在一个单独类的测试完成运行之后被调用的类方法
    @classmethod
    def tearDownClass(cls):
        print("TestListMethodsCase tearDownClass....")


if __name__ == '__main__':
    unittest.main()


