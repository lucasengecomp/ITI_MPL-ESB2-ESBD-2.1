import unittest
from Roman_samples06 import RomanSamples

class RomanToIntTest(unittest.TestCase):

    def test_roman01(self):
    	self.assertEqual(RomanSamples.RomanToInt("I"), 1)

    def test_roman02(self):
    	self.assertEqual(RomanSamples.RomanToInt("V"), 5)

    def test_roman03(self):
    	self.assertEqual(RomanSamples.RomanToInt("X"), 10)

    def test_roman04(self):
    	self.assertEqual(RomanSamples.RomanToInt("L"), 50)

    def test_roman05(self):
    	self.assertEqual(RomanSamples.RomanToInt("C"), 100)

    def test_roman06(self):
    	self.assertEqual(RomanSamples.RomanToInt("D"), 500)

    def test_roman07(self):
    	self.assertEqual(RomanSamples.RomanToInt("M"), 1000)

    def test_roman08(self):
        self.assertEqual(RomanSamples.RomanToInt("P"), -1)

    def test_roman09(self):
        self.assertEqual(RomanSamples.RomanToInt("II"), 2)
    
    def test_roman10(self):
        self.assertEqual(RomanSamples.RomanToInt("VI"), 6)

    def test_roman11(self):
        self.assertEqual(RomanSamples.RomanToInt("IV"), 4)

    def test_roman12(self):
        self.assertEqual(RomanSamples.RomanToInt("III"), 3)

    def test_roman13(self):
        self.assertEqual(RomanSamples.RomanToInt("IIII"), -1)