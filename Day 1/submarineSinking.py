def intSum(inputList):
	newList = list(map(int, inputList))
	return sum(newList)


def findIncreasing(file):
	f = open(file)
	fileLines = f.readlines()
	for i in range(1,len(fileLines)):
		if int(fileLines[i]) > int(fileLines[i-1]):
			greaterThanLast += 1

	print(fileLines[-1])
	print(greaterThanLast)
	f.close()

def threeMeasurementSum(file):
	f = open(file)
	fileLines = f.readlines()
	increasingWindow = 0
	for i in range(0, len(fileLines)-2):
		firstWindow = intSum(fileLines[i:i+3])
		secondWindow = intSum(fileLines[i+1:i+4])
		#print(f"{firstWindow=}, {secondWindow=}")
		if firstWindow < secondWindow:
			increasingWindow += 1
	print(f"{increasingWindow=}")
	f.close()
	return 0 
threeMeasurementSum("textDocs/inputSinking.txt")

