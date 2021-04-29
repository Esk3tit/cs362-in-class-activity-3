import unittest
import calculator


# Class
class TestCalc(unittest.TestCase):

    # Test addition
    def test_add(self):
        self.assertEqual(calculator.add(1, 1), 2)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(1.1, 3.3), 4.4)

    # Test subtraction (last test case fails)
    def test_sub(self):
        self.assertEqual(calculator.sub(1, 1), 0)
        self.assertEqual(calculator.sub(-1, 1), -2)
        self.assertEqual(calculator.sub('1.1', 3.3), 4.4)

    # Test multiplication (first case fails)
    def test_mult(self):
        self.assertEqual(calculator.mult(1, 1), 0)
        self.assertEqual(calculator.mult(0, 1), 0)
        self.assertEqual(calculator.mult(1.5, 2), 3)

    # Test division (third case fails)
    def test_div(self):
        self.assertEqual(calculator.div(1, 1), 1)
        self.assertEqual(calculator.div(0, 1), 0)
        self.assertEqual(calculator.div(1, 0), 0)
        self.assertEqual(calculator.div(1, 0), float("nan"))


if __name__ == "__main__":
    unittest.main()
