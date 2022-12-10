import unittest

class Calculator:
    def init(self):
        pass

    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b


class TestCalculator(unittest.TestCase):
    def test_add(self):
            '''Test case function for addition'''
            self.calc\
                = Calculator()
            result = self.calc.add(4, 7)
            expected = 11
            self.assertEqual(result, expected)

    def test_sub(self):
            '''Test case function for subtraction'''
            self.calc = Calculator()
            result = self.calc.sub(10, 5)
            expected = 5
            self.assertEqual(result, expected) @ unittest.skip('Some reason')

    def test_mul(self):
            '''Test case function for multiplication'''
            self.calc = Calculator()
            result = self.calc.mul(3, 7)
            expected = 21
            self.assertEqual(result, expected)

