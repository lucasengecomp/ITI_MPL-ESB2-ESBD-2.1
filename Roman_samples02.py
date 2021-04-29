class RomanSamples:

	@staticmethod
	def RomanToInt(str):		
		romanCaracter = {
			"I" : 1,
			"V" : 5,
			"X" : 10,
			"L" : 50,
			"C" : 100,
			"D" : 500,
			"M" : 1000
		}

		if str in romanCaracter.keys():
			return romanCaracter[str]
		return []

