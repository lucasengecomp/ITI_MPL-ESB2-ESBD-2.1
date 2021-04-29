import unittest
from Roman_samples02 import RomanSamples

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