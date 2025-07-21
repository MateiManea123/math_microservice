import unittest
from app.functions import nth_fibonacci, factorial, poww

class TestMathFunctions(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(nth_fibonacci(0), 0)
        self.assertEqual(nth_fibonacci(1), 1)
        self.assertEqual(nth_fibonacci(5), 5)
        self.assertEqual(nth_fibonacci(10), 55)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    def test_poww(self):
        self.assertEqual(poww(2, 3), 8)
        self.assertEqual(poww(5, 0), 1)  # <- atenție! actuala implementare e invalidă pt p=0
        self.assertEqual(poww(10, 2), 100)
        self.assertEqual(poww(3, 4), 81)

if __name__ == '__main__':
    unittest.main()
