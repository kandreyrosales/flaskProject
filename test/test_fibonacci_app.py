import unittest
from app import complete_fibonacci


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(complete_fibonacci(5), [0, 1, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
