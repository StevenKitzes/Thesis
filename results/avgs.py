# This script scans a range of tests that were performed with the same parameters, gathers
# relevant data from those tests, and averages the results.  The 'help' output below gives
# directions on how to use this script and what parameters are required.

import re
import sys

if sys.argv[1]:
	if sys.argv[1] == "-h":
		print("Expected arguments are all mandatory and must appear in order.")
		print("")
		print("    python avgs.py [num] [con] [name] [which] [howmany]")
		print("")
		print("[num]                    - how many requests were made in each Apache Bench test run")
		print("[con]                    - concurrency level for the test run batch")
		print("[name]                   - name of the test script that was being evaluated")
		print("[which]                  - 'node' or 'php' (can't average both together)")
		print("[howmany]                - how many test result files to include")
		print("")
		print("This script ASSUMES that file names are well formed, and that all")
		print("files are present, from 0 through the number (howmany) given, exclusive.")
		print("Error checking is not provided, so please be sure to double check your")
		print("numbers and enter them in the correct order!")
		sys.exit()

bandwidths = []		# in req per sec
concurrentMeans = []# in req per sec
means = []			# in ms
longests = []		# in ms

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]
which = sys.argv[4]			# 'node' or 'php'
howmany = int(sys.argv[5])

print("Calculating some averages over " + num + " requests with " + con + " concurrency")
print("    for test '" + name + "' on " + which + " . . .")

for i in range(0, howmany):
	incomingFile = which + "_" + num + "-" + con + "-" + name + "_" + str(i) + ".txt"
	# print("Opening file: " + incomingFile)
	
	f = open(incomingFile)
	fContent = f.read()
	
	# print("File content loaded.")
	
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

#print("")
#print("bandwidths: " + str(bandwidths))
#print("concurrentMeans: " + str(concurrentMeans))
#print("means: " + str(means))
#print("longests: " + str(longests))

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