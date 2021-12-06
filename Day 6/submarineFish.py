# Finding a way to simulate the number of fish
from collections import defaultdict

def readDataList(file):
	f = open(file)
	listLine = f.readline()
	outputList = list(map(int, listLine.split(',')))
	return outputList

# Get a list of fish
# Each day, the internal clock on the fish goes down by one
# If the fish is at 0, it will reset to 6 and append an 8 onto the list

defaultDictionary = defaultdict(int)

dataList = readDataList("inputLanternfish.txt")
#print(f"{numberOfFish=}")

for number in dataList:
	if number not in defaultDictionary:
		defaultDictionary[number] = 0
	defaultDictionary[number] += 1

for day in range(2):
	#print(day, len(defaultDictionary))
	newDefaultDict = defaultdict(int)
	print(defaultDictionary.items())
	for k,cnt in defaultDictionary.items():
		if k == 0:
			newDefaultDict[6] += cnt
			newDefaultDict[8] += cnt
		else:
			newDefaultDict[k-1] += cnt
	defaultDictionary = newDefaultDict
print(sum(defaultDictionary.values()))



