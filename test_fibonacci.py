import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "Negative numbers are not allowed")

        with self.assertRaises(ValueError) as context:
            fibonacci(1001)
        self.assertEqual(str(context.exception), "Value too large")

if __name__ == '__main__':
    unittest.main()
