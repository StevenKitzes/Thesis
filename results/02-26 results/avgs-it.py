# This script scans a range of tests that were performed with the same parameters, over a range
# of concurrencies begging at 2 and increasing by powers of two, then gathers relevant data from
# those tests, and averages the results.  The 'help' output below gives directions on how to use
# this script and what parameters are required.
# NOTE: this script assumes equivalent tests are available for averaging in both PHP and Node

import re
import sys

if sys.argv[1]:
	if sys.argv[1] == "-h":
		print("Expected arguments are all mandatory and must appear in order.")
		print("")
		print("    python avgs.py [num] [con] [name] [which] [howmany]")
		print("")
		print("[num]                    - how many requests were made in each Apache Bench test run")
		print("[maxcon]                    - concurrency level for the test run batch")
		print("[name]                   - name of the test script that was being evaluated")
		print("[howmany]                - how many test result files to include")
		print("")
		print("This script ASSUMES that file names are well formed, and that all")
		print("files are present, from 0 through the number (howmany) given, exclusive.")
		print("Error checking is not provided, so please be sure to double check your")
		print("numbers and enter them in the correct order!")
		sys.exit()

num = sys.argv[1]
maxcon = int(sys.argv[2])
name = sys.argv[3]
howmany = int(sys.argv[4])

print("concurrency,avg node bandwidth,avg node concurrent mean,avg node mean,avg node longest,avg php bandwidth,avg php concurrent mean,avg php mean,avg php longest")

con = 2
while con <= maxcon:
	nodeBandwidths = []		# in req per sec
	phpBandwidths = []		# in req per sec
	
	nodeConcurrentMeans = []# in req per sec
	phpConcurrentMeans = []# in req per sec
	
	nodeMeans = []			# in ms
	phpMeans = []			# in ms
	
	nodeLongests = []		# in ms
	phpLongests = []		# in ms
	
#	print("Calculating some averages over " + num + " requests with " + con + " concurrency")
#	print("    for test '" + name + "' on " + which + " . . .")
	
	for i in range(0, howmany):
		incomingNode = "node_" + num + "-" + str(con) + "-" + name + "_" + str(i) + ".txt"
		incomingPhp = "php_" + num + "-" + str(con) + "-" + name + "_" + str(i) + ".txt"
		# print("Opening file: " + incomingFile)
		
		fNode = open(incomingNode)
		fPhp = open(incomingPhp)
		fContentNode = fNode.read()
		fContentPhp = fPhp.read()
		
		# print("File content loaded.")
		
		bandwidthRE = "[0-9][\.\d]*(?=(\s\[#))"
		bandwidthMatchGroupNode = re.search(bandwidthRE, fContentNode)
		nodeBandwidths.append(float(bandwidthMatchGroupNode.group(0)))
		bandwidthMatchGroupPhp = re.search(bandwidthRE, fContentPhp)
		phpBandwidths.append(float(bandwidthMatchGroupPhp.group(0)))
		
		concurrentMeanRE = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean,))"
		concurrentMeanMatchGroupNode = re.search(concurrentMeanRE, fContentNode)
		nodeConcurrentMeans.append(float(concurrentMeanMatchGroupNode.group(0)))
		concurrentMeanMatchGroupPhp = re.search(concurrentMeanRE, fContentPhp)
		phpConcurrentMeans.append(float(concurrentMeanMatchGroupPhp.group(0)))
		
		meanRE = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean\)))"
		meanMatchGroupNode = re.search(meanRE, fContentNode)
		nodeMeans.append(float(meanMatchGroupNode.group(0)))
		meanMatchGroupPhp = re.search(meanRE, fContentPhp)
		phpMeans.append(float(meanMatchGroupPhp.group(0)))
		
		longestRE = "(?<=(100%))\s*[0-9][\.\d]*(?=(\s))"
		longestMatchGroupNode = re.search(longestRE, fContentNode)
		nodeLongests.append(float(longestMatchGroupNode.group(0)))
		longestMatchGroupPhp = re.search(longestRE, fContentPhp)
		phpLongests.append(float(longestMatchGroupPhp.group(0)))
		
	#print("")
	#print("bandwidths: " + str(bandwidths))
	#print("concurrentMeans: " + str(concurrentMeans))
	#print("means: " + str(means))
	#print("longests: " + str(longests))
	
	bwTotN = 0
	cmTotN = 0
	mTotN = 0
	lTotN = 0
	
	bwTotP = 0
	cmTotP = 0
	mTotP = 0
	lTotP = 0
	
	items = len(nodeBandwidths)
	
	for i in range(0, items):
		bwTotN += nodeBandwidths[i]
		cmTotN += nodeConcurrentMeans[i]
		mTotN += nodeMeans[i]
		lTotN += nodeLongests[i]
		bwTotP += phpBandwidths[i]
		cmTotP += phpConcurrentMeans[i]
		mTotP += phpMeans[i]
		lTotP += phpLongests[i]
	
	finalBandwidthNode = bwTotN / items
	finalConcurrentMeanNode = cmTotN / items
	finalMeanNode = mTotN / items
	finalLongestNode = lTotN / items
	finalBandwidthPhp = bwTotP / items
	finalConcurrentMeanPhp = cmTotP / items
	finalMeanPhp = mTotP / items
	finalLongestPhp = lTotP / items
	
	print(str(con) + "," + str(finalBandwidthNode) + "," + str(finalConcurrentMeanNode) + "," + str(finalMeanNode) + "," + str(finalLongestNode) + "," + str(finalBandwidthPhp) + "," + str(finalConcurrentMeanPhp) + "," + str(finalMeanPhp) + "," + str(finalLongestPhp))
	
	con *= 2