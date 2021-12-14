import sys
from collections import defaultdict, Counter

f = open("inputCrabs.txt")
allLines = [int(x) for x in f.read().strip().split(',')]
allLines.sort()
ans = 0
def C2(d):
    return d*(d+1)/2

best = 1e9
for med in range(2000):
    score = 0
    for x in allLines:
        d = abs(x-med)
        score += C2(d)
    if score < best:
        best = score

print(best)
'''
med = allLines[len(allLines)//2]
for element in allLines:
    ans += abs(element-med)
print(ans)
'''