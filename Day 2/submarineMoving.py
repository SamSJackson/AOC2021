def findPosition(file):
	position = [0,0]
	aim = 0
	f = open(file)
	fileLines = f.readlines()
	for movement in fileLines:
		splitMovement = movement.split()
		if splitMovement[0] == "forward":
			position[0] += int(splitMovement[1])
			position[1] += aim*int(splitMovement[1])
		elif splitMovement[0] == "down":
			aim += int(splitMovement[1])
		elif splitMovement[0] == "up":
			aim -= int(splitMovement[1])
	print(position)
	print(position[0]*position[1])
	print(f"{position[0]=}, {position[1]=}")
	print(f"{position[0]*position[1]=}")
	f.close()
	return position[0]*position[1]

findPosition("textDocs/inputMoving.txt")
