from fractions import Fraction as frac
import unittest

class Calculator:
    def add(self, fr1, fr2):
    	return str(frac(fr1) + frac(fr2))
    	
    def minus(self, fr1, fr2):
    	return str(frac(fr1) - frac(fr2))
    	
    def multiply(self, fr1, fr2):
    	return str(frac(fr1) * frac(fr2))
    	
    def divide(self, fr1, fr2):
    	return str(frac(fr1) / frac(fr2))
    
    
class CalculatorTestCase(unittest.TestCase):
    def testZeroPlusZero(self):
        calculator = Calculator()
        result = calculator.add('0','0')
        self.assertEquals(result, '0')
        
    def testAdd(self):
        calculator = Calculator()
        result = calculator.add('5/4','9/8')
        self.assertEquals(result, '19/8')
    
    def testMinus(self):
        calculator = Calculator()
        result = calculator.minus('2/3','1/4')
        self.assertEquals(result, '5/12')
        
    def testMultiply(self):
        calculator = Calculator()
        result = calculator.multiply('2/3','5/15')
        self.assertEquals(result, '2/9')
        
    def testDivide(self):
        calculator = Calculator()
        result = calculator.divide('2/6','4/2')
        self.assertEquals(result, '1/6')

unittest.main()