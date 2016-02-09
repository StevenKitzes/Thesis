import re
import sys

print("Calculating some averages from given input files . . .")

bandwidths = []		# in req per sec
concurrentMeans = []# in req per sec
means = []			# in ms
longests = []		# in ms

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]
which = sys.argv[4]

for i in range(0, 5):
	incomingFile = which + "_" + num + "-" + con + "-" + name + "_" + str(i) + ".txt"
	print("Opening file: " + incomingFile)
	
	f = open(incomingFile)
	fContent = f.read()
	
	print("File content loaded.")
	
	bandwidthRE = "[0-9][\.\d]*(?=(\s\[#))"
	bandwidthMatchGroup = re.search(bandwidthRE, fContent)
	bandwidths.append(float(bandwidthMatchGroup.group(0)))
	
	concurrentMeanRE = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean,))"
	concurrentMeanMatchGroup = re.search(concurrentMeanRE, fContent)
	concurrentMeans.append(float(concurrentMeanMatchGroup.group(0)))
	
	meanRE = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean\)))"
	meanMatchGroup = re.search(meanRE, fContent)
	means.append(float(meanMatchGroup.group(0)))
	
	longestRE = "(?<=(100%))\s*[0-9][\.\d]*(?=(\s))"
	longestMatchGroup = re.search(longestRE, fContent)
	longests.append(float(longestMatchGroup.group(0)))

print("")
print("bandwidths: " + str(bandwidths))
print("concurrentMeans: " + str(concurrentMeans))
print("means: " + str(means))
print("longests: " + str(longests))

bwTot = 0
cmTot = 0
mTot = 0
lTot = 0

items = len(bandwidths)

for i in range(0, items):
	bwTot = bwTot + bandwidths[i]
	cmTot = cmTot + concurrentMeans[i]
	mTot = mTot + means[i]
	lTot = lTot + longests[i]

finalBandwidth = bwTot / items
finalConcurrentMean = cmTot / items
finalMean = mTot / items
finalLongest = lTot / items

print("")
print("Avg bandwidth:       " + str(finalBandwidth))
print("Avg concurrent mean: " + str(finalConcurrentMean))
print("Avg mean:            " + str(finalMean))
print("Avg longest:         " + str(finalLongest))