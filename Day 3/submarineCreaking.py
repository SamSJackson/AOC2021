def findOxygenRating(inputList : list, position=0):
	if len(inputList) == 1:
		return inputList[0]
	# if elementNumber >= 0, 1.
	# if elementNumber < 0, 0
	elementNumber = 0
	recursiveList = []
	for element in inputList:
		if element[position] == "1":
			elementNumber += 1
		else:
			elementNumber -= 1

	desiredElement = "1" if elementNumber >= 0 else "0"

	for element in inputList:
		if element[position] == desiredElement:
			recursiveList.append(element)
	return findOxygenRating(recursiveList, position=position+1)

def findC02Rating(inputList, position=0):
	if len(inputList) == 1:
		return inputList[0]
	# if elementNumber >= 0, 1.
	# if elementNumber < 0, 0
	elementNumber = 0
	recursiveList = []
	for element in inputList:
		if element[position] == "1":
			elementNumber += 1
		else:
			elementNumber -= 1
	# Need opposite of most common number
	leastCommon = "0" if elementNumber >= 0 else "1"

	for element in inputList:
		if element[position] == leastCommon:
			recursiveList.append(element)
	return findC02Rating(recursiveList, position=position+1)


def findGammaRate(file):
	f = open(file)
	allLines = f.readlines()
	gammaRate = ""
	epsilonRate = ""
	for i, value in enumerate(allLines[0].strip()):
		#add if 1, take away if 0
		mostCommon = 0
		try:
			for element in allLines:
				if element[i] == "1":
					mostCommon += 1
				else:
					mostCommon -= 1
			if mostCommon > 0:
				gammaRate += "1"
				epsilonRate += "0"
			else:
				gammaRate += "0"
				epsilonRate += "1"
		except Exception as e:
			print(e)
			print(value)
			print(i)
	#print(f"{gammaRate=}, {epsilonRate=}")
	decimalGamma = int(gammaRate, 2)
	decimalEpsilon = int(epsilonRate, 2)
	#print(f"{decimalGamma=}, {decimalEpsilon=}")
	#print(f"{decimalGamma*decimalEpsilon=}")
	f.close()
	return [gammaRate, epsilonRate]

gammaRate, epsilonRate = findGammaRate("textDocs/inputCreaking.txt")
print(f"{gammaRate=}")
print(f"{epsilonRate=}")
def findRatings(file):
	f = open(file)
	allLines = f.readlines()
	oxygenRating = findOxygenRating(allLines).strip()
	carbonRating = findC02Rating(allLines).strip()
	print(f"{oxygenRating=}")
	print(f"{int(oxygenRating, 2)=}")
	print(f"{carbonRating=}")
	print(f"{int(carbonRating, 2)=}")
	safetyRating = int(oxygenRating, 2) * int(carbonRating, 2)
	print(f"{safetyRating=}")

findRatings("textDocs/inputCreaking.txt")
