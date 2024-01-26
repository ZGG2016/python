import unittest


class ExpectedFailureTestCase(unittest.TestCase):
    # 表明这个测试预计失败，但不会算进 TestResult 的失败里
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


if __name__ == '__main__':
    unittest.main()
