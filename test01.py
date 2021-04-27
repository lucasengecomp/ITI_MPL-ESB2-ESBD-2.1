import unittest
from Roman_samples01 import RomanSamples

class RomanToIntTest(unittest.TestCase):

    def test_roman01(self):
    	self.assertEqual(RomanSamples.RomanToInt("I"), 1)