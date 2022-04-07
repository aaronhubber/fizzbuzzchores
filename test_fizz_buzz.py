
import unittest

from fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self): 
        self.fizz_buzz = 1
        self.fizz_buzz_3 =3
        self.fizz_buzz_6 = 6
        self.fizz_buzz_5 = 5
        self.fizz_buzz_15 = 15
        self.fizz_buzz_30 = 30
       
    
    def test_fizz_buzz_return_value(self):
        value = fizz_buzz(self.fizz_buzz)
        self.assertEqual("1", value)

    def test_fizz_buzz_return_value_3(self):
        value = fizz_buzz(self.fizz_buzz_3)
        self.assertEqual("fizz", value)
    
    def test_fizz_buzz_return_value_6(self):
        value = fizz_buzz(self.fizz_buzz_6) #user input could go in here
        self.assertEqual("fizz", value)

    def test_fizz_buzz_return_value_5(self):
        value = fizz_buzz(self.fizz_buzz_5)
        self.assertEqual("buzz", value)
    
    def test_fizz_buzz_return_value_15(self):
        value = fizz_buzz(self.fizz_buzz_15)
        self.assertEqual("fizzbuzz", value)
    
    def test_fizz_buzz_return_value_30(self):
        value = fizz_buzz(self.fizz_buzz_30)
        self.assertEqual("fizzbuzz", value)
    
    def test_fizz_buzz_return_value_7(self):
        value = fizz_buzz(0)
        self.assertEqual("0", value)
    
    

