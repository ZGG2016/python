import unittest


# 当你的几个测试之间的差异非常小，例如只有某些形参不同时，
# unittest 允许你使用 subTest() 上下文管理器在一个测试方法体的内部区分它们。
# 如果不使用子测试，程序遇到第一次错误之后就会停止
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    unittest.main()
