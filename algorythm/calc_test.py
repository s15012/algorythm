#!/usr/bin/python3

import calc
import unittest

class CalcTest(unittest.TestCase):

    def test_isNumeric_true(self):
        obj = calc.Calc()
        self.assertTrue(obj.isNumeric('0'))
        self.assertTrue(obj.isNumeric('1'))
        self.assertTrue(obj.isNumeric('2'))
        self.assertTrue(obj.isNumeric('3'))
        self.assertTrue(obj.isNumeric('4'))
        self.assertTrue(obj.isNumeric('5'))
        self.assertTrue(obj.isNumeric('6'))
        self.assertTrue(obj.isNumeric('7'))
        self.assertTrue(obj.isNumeric('8'))
        self.assertTrue(obj.isNumeric('9'))
if __name__ == '__main__':
    unitetest.main()
