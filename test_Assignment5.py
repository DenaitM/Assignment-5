import unittest
from Assignment5 import tempFahrenheitToCelsius
from Assignment5 import fibonacciNumber


class TestAssignment5(unittest.TestCase):
    def test_tempFahrenheitToCelsius(self):
        self.assertEqual(tempFahrenheitToCelsius(5), -15)
        self.assertEqual(tempFahrenheitToCelsius(50), 10)
        self.assertEqual(tempFahrenheitToCelsius(20), -6.666666666666667)

    
    def testfibonacciNumber(self):
        self.assertEqual(fibonacciNumber(0), 0)
        self.assertEqual(fibonacciNumber(1), 1)
        self.assertEqual(fibonacciNumber(2), 1)
        

if __name__ == '__main__':
    unittest.main()
    
