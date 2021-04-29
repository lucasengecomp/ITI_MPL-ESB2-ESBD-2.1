class RomanSamples:

	@staticmethod
	def RomanToInt(input):		
		romanCaracter = {
			"I" : 1,
			"V" : 5,
			"X" : 10,
			"L" : 50,
			"C" : 100,
			"D" : 500,
			"M" : 1000
		}
		temp = []
		for i in input:
			if i not in romanCaracter:
				return -1
			temp.append(romanCaracter[i])

		result = temp[0]
		for j, element in enumerate(temp[:-1]):
			if temp[j + 1] <= element:
				result = temp[j + 1] + result
			else:
				result = temp[j + 1] - result
		return result