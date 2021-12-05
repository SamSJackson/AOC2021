# submarineFlooring.py

# First part, only consider horizontal lines (x_1 = x_2 or y_1 = y_2)

class Point:

	def __init__(self, x, y):
		self._x = x
		self._y = y
		self._timesCrossed = 0

	# Overriding print
	def __str__(self):
		return str(self._timesCrossed)

	@property
	def timesCrossed(self):
		return self._timesCrossed
	
	def setCrossed(self, crossed : bool):
		self._timesCrossed += 1

def createBoard(boardX : int, boardY : int):
	overallBoard = []
	boardSquare = max(boardX, boardY)
	for i in range(boardSquare+1):
		rowLine = []
		for j in range(boardSquare+1):
			rowLine.append(Point(j, i))
		overallBoard.append(rowLine)
	return overallBoard

def findAllLines(file):
	f = open(file)
	allLines = f.readlines()
	allStraightLines = []
	maxNumX = 0
	maxNumY = 0
	for line in allLines:
		arrowSplit = line.split('->')
		linePoints = []
		x1,y1 = list(map(int, arrowSplit[0].strip().split(',')))
		x2,y2 = list(map(int, arrowSplit[1].strip().split(',')))
		if max(x1, x2) > maxNumX:
			maxNumX = max(x1, x2)
		if max(y1, y2) > maxNumY:
			maxNumY = max(y1, y2)
		allStraightLines.append(line.strip())
	f.close()
	return allStraightLines, maxNumX, maxNumY

# Obtaining all straight lines
def findStraightLines(file):
	f = open(file)
	allLines = f.readlines()
	allStraightLines = []
	maxNumX = 0
	maxNumY = 0
	for line in allLines:
		arrowSplit = line.split('->')
		linePoints = []
		x1,y1 = list(map(int, arrowSplit[0].strip().split(',')))
		x2,y2 = list(map(int, arrowSplit[1].strip().split(',')))
		if x1==x2 or y1==y2:
			if max(x1, x2) > maxNumX:
				maxNumX = max(x1, x2)
			if max(y1, y2) > maxNumY:
				maxNumY = max(y1, y2)
			allStraightLines.append(line.strip())
	f.close()
	return allStraightLines, maxNumX, maxNumY

def drawLines(board, linesList : list):
	linesCrossed = 0
	for line in linesList:
		arrowSplit = line.split('->')
		x1,y1 = list(map(int, arrowSplit[0].strip().split(',')))
		x2,y2 = list(map(int, arrowSplit[1].strip().split(',')))
		if x1 == x2 and y1 == y2:
			if board[x1][y1].timesCrossed == 1:
				linesCrossed += 1
			board[x1][y1].setCrossed(1)
		elif x1 == x2:
			for i in range(min(y1, y2), max(y1,y2)+1):
				if board[i][x1].timesCrossed == 1:
					linesCrossed += 1
				board[i][x1].setCrossed(1)
		elif y1 == y2: 
			for i in range(min(x1,x2), max(x1,x2)+1):
				if board[y1][i].timesCrossed == 1:
					linesCrossed += 1
				board[y1][i].setCrossed(1)
	for i, row in enumerate(board):
		for j, point in enumerate(row):
			print(point, end=" ")
		print()

	return linesCrossed

def drawLinesDiagonal(board, allLinesList : list):
	linesCrossed = 0
	for line in allLinesList:
		arrowSplit = line.split('->')
		x1,y1 = list(map(int, arrowSplit[0].strip().split(',')))
		x2,y2 = list(map(int, arrowSplit[1].strip().split(',')))
		if x1 == x2 and y1 == y2:
			if board[x1][y1].timesCrossed == 1:
				linesCrossed += 1
			board[x1][y1].setCrossed(1)
		elif x1 == x2:
			for i in range(min(y1, y2), max(y1,y2)+1):
				if board[i][x1].timesCrossed == 1:
					linesCrossed += 1
				board[i][x1].setCrossed(1)
		elif y1 == y2: 
			for i in range(min(x1,x2), max(x1,x2)+1):
				if board[y1][i].timesCrossed == 1:
					linesCrossed += 1
				board[y1][i].setCrossed(1)

		# Need to deal with diagonal now
		# Stepping up
		elif y1 < y2:
			# Stepping up and right
			if x1 < x2:
				for i in range(abs(y2-y1)+1):
					if board[y1+i][x1+i].timesCrossed == 1:
						linesCrossed += 1
					board[y1+i][x1+i].setCrossed(1)
			# Stepping up and left
			elif x1 > x2:
				for i in range(abs(y2-y1)+1):
					if board[y1+i][x1-i].timesCrossed == 1:
						linesCrossed += 1
					board[y1+i][x1-i].setCrossed(1)
		# Stepping down
		elif y1 > y2:
			# Stepping down and right
			if x1 < x2:
				for i in range(abs(y1-y2)+1):
					if board[y1-i][x1+i].timesCrossed == 1:
						linesCrossed += 1
					board[y1-i][x1+i].setCrossed(1)
			# Stepping down and left
			elif x1 > x2:
				for i in range(abs(y1-y2)+1):
					if board[y1-i][x1-i].timesCrossed == 1:
						linesCrossed += 1
					board[y1-i][x1-i].setCrossed(1)
	return linesCrossed



allLines, boardX, boardY = findAllLines("inputHydrothermal.txt")

board = createBoard(boardX, boardY)
linesCrossed = drawLinesDiagonal(board, allLines)
print(f"{linesCrossed=}")


# Don't need to filter for the diagonal lines because file
# only contains straight, or lines on a diagonal


