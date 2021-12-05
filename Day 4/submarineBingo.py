class BingoNumber:
	def __init__(self, value):
		self.value = value
		self.marked = False

	def setMarked(self, isMarked : bool):
		self.marked = isMarked


def printMatrix(matrix):
	for row in matrix:
		for item in row:
			print(item.value, end=" ")
		print()

def checkMatrixRow(matrix):
	# Check horizontal
	for row in matrix:
		counter = 0
		while row[counter].marked == True and counter < 5:
			if counter == 4:
				return True
			counter += 1
	return False

def checkMatrixColumn(matrix):
	# Check vertical
	for i in range(len(matrix)):
		counter = 0
		while matrix[counter][i].marked == True and counter < 5:
			if counter == 4:
				return True
			counter += 1
	return False

def markNumbers(markedNumbers : list, allMatrices):
	for i, number in enumerate(markedNumbers):
		for matrix in allMatrices:
			for row in matrix:
				for item in row:
					if item.value == number:
						item.setMarked(True)
			if checkMatrices(matrix):
				return [matrix, number]

def checkMatrices(matrix):
	if checkMatrixRow(matrix) or checkMatrixColumn(matrix):
		return True

def getUnmarkedSum(matrix):
	totalSum = 0
	for row in matrix:
		for item in row:
			if item.marked == False:
				totalSum += int(item.value)
	return totalSum

def findWinner(file):
	f = open(file)
	allLines = f.readlines()
	# First line contains the information on numbers that are marked
	markedNumbers = allLines[0].strip().split(',')

	# Format of matrices list is triple-nested list
	# First list, contains all matrices
	# Nest list, contains each matrix
	# Double nested list, contains each row of matrix
	allMatrices = []
	# Now need to obtain each five by five matrices
	for i in range(2, len(allLines)-4, 6):
		matrix = [allLines[x].strip().split() for x in range(i, i+5)]

		# Each item cast to BingoNumber object
		for i, row in enumerate(matrix):
			for j, item in enumerate(row):
				matrix[i][j] = BingoNumber(item)
		allMatrices.append(matrix)
	f.close()
	return [allMatrices, markedNumbers]
	# Remove return if you want to know first winner
	winningMatrix, winningNumber = markNumbers(markedNumbers, allMatrices)
	printMatrix(winningMatrix)
	totalSum = getUnmarkedSum(winningMatrix) * int(winningNumber)
	print(f"{totalSum=}")

# How to find last board to win
# Could make recursive method that removes a matrix when it wins
# fuck it i do that
def findWorstMatrix(allMatrices, markedNumbers, currentNumberWinning=0):
	if len(allMatrices) == 1:
		# Need to find what number it is when this matrix finishes
		winningMatrix, winningNumber = markNumbers(markedNumbers, allMatrices)
		printMatrix(allMatrices[0])
		totalSum = getUnmarkedSum(allMatrices[0])
		returnSum = totalSum * int(winningNumber)
		return allMatrices[0], returnSum
	else:
		winningMatrix, winningNumber = markNumbers(markedNumbers, allMatrices)
		winningLocation = allMatrices.index(winningMatrix)

		allMatrices.pop(winningLocation)
		return findWorstMatrix(allMatrices, markedNumbers)

allMatrices, markedNumbers = findWinner("textDocs/inputBingo.txt")

answerMatrix, totalSum = findWorstMatrix(allMatrices, markedNumbers)
print(totalSum)

