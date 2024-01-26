import unittest


class TestStringMethodsCase(unittest.TestCase):
    # 在一个单独类中的测试运行之前被调用的类方法
    # 当测试套件遇到来自新类的测试时则来自之前的类（如果存在）的 tearDownClass() 会被调用，
    # 然后再调用来自新类的 setUpClass()
    @classmethod
    def setUpClass(cls):
        print("TestStringMethodsCase setUpClass....")
        print(cls)

    def test_upper(self):
        self.assertEqual('Foo'.upper(), 'FOO')
        # self.assertEqual('Foo'.upper(), 'Foo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    # 在一个单独类的测试完成运行之后被调用的类方法
    @classmethod
    def tearDownClass(cls):
        print("TestStringMethodsCase tearDownClass....")


if __name__ == '__main__':
    unittest.main()