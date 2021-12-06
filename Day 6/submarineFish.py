# Finding a way to simulate the number of fish

def readDataList(file):
	f = open(file)
	listLine = f.readline()
	outputList = list(map(int, listLine.split(',')))
	return outputList

# Get a list of fish
# Each day, the internal clock on the fish goes down by one
# If the fish is at 0, it will reset to 6 and append an 8 onto the list


# This could be recursive
def ageFish(fishList : list, days : int, counter=1):
	if days == 0:
		return len(fishList)
	else:
		for i, value in enumerate(fishList):
			if value == 0:
				fishList[i]=6
				fishList.append(9)
			else:
				fishList[i] -= 1
		#print(f"After {counter} days: {fishList}")
		print(f"Day: {counter}")
		return ageFish(fishList, days-1, counter+1)

dataList = readDataList("inputLanternfish2.txt")
#numberOfFish = ageFish(dataList, 256)
#print(f"{numberOfFish=}")



