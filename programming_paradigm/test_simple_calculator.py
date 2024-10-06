import unittest
from simple_calculator import SimpleCalculator

class testSimpleCalculator(unittest.TestCase):
  def setUp(self):
    self.calc = SimpleCalculator()
  def test_addition(self):
    self.assertEqual(self.calc.add(4,5) , 9)
    self.assertEqual(self.calc.add(-1,1) , 0)
    self.assertEqual(self.calc.add(-1,-1) , -2)
  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(5,3) , 2)
    self.assertEqual(self.calc.subtract(3,5) , -2)
    self.assertEqual(self.calc.subtract(-3,3) , -6)
    self.assertEqual(self.calc.subtract(-3,-3) , 0)

  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(4,5) , 20)
    self.assertEqual(self.calc.multiply(-4,5) , -20)
    self.assertEqual(self.calc.multiply(-4,-5) , 20)


  def test_division(self):
    self.assertEqual(self.calc.divide(4,0), None)
    self.assertEqual(self.calc.divide(4,2) , 2)