# This script scans a range of tests that were performed with the multi.py script and averages
# the results.  The 'help' output below gives directions on how to use this script and what
# parameters are required.

import re
import sys

def usageGuide():
	print("There is only one argument and it is mandatory.")
	print("")
	print("    python avgs.py [howmany]")
	print("")
	print("[howmany] - how many test result files to include")
	print("")
	print("This script ASSUMES that file names are well formed, and that all")
	print("files are present, from 0 through the number [howmany] given, exclusive.")
	print("Error checking is not provided, so please be sure to double check your")
	print("numbers and enter them in the correct order!")
	sys.exit()

if sys.argv[1]:
	if sys.argv[1] == "-h":
		usageGuide()
else:
	usageGuide()

node_db_bandwidths = []
node_regexp_bandwidths = []
node_static_bandwidths = []
php_db_bandwidths = []
php_regexp_bandwidths = []
php_static_bandwidths = []

node_db_concurrentMeans = []
node_regexp_concurrentMeans = []
node_static_concurrentMeans = []
php_db_concurrentMeans = []
php_regexp_concurrentMeans = []
php_static_concurrentMeans = []

node_db_means = []
node_regexp_means = []
node_static_means = []
php_db_means = []
php_regexp_means = []
php_static_means = []

node_db_longests = []
node_regexp_longests = []
node_static_longests = []
php_db_longests = []
php_regexp_longests = []
php_static_longests = []

howmany = int(sys.argv[1])

#print("Calculating some averages over " + howmany + " batches")

regexp_bandwidth = "[0-9][\.\d]*(?=(\s\[#))"
regexp_concurrentMean = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean,))"
regexp_mean = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean\)))"
regexp_longest = "(?<=(100%))\s*[0-9][\.\d]*(?=(\s))"

for i in range(0, howmany):
	node_db_incomingFile		= "n_database_" + str(i) + ".txt"
	node_regexp_incomingFile	= "n_regexp_" + str(i) + ".txt"
	node_static_incomingFile	= "n_static_" + str(i) + ".txt"
	php_db_incomingFile			= "p_database_" + str(i) + ".txt"
	php_regexp_incomingFile		= "p_regexp_" + str(i) + ".txt"
	php_static_incomingFile		= "p_static_" + str(i) + ".txt"
	
	node_db_file		= open(node_db_incomingFile)
	node_regexp_file	= open(node_regexp_incomingFile)
	node_static_file	= open(node_static_incomingFile)
	php_db_file			= open(php_db_incomingFile)
	php_regexp_file		= open(php_regexp_incomingFile)
	php_static_file		= open(php_static_incomingFile)
	
	node_db_content			= node_db_file.read()
	node_regexp_content		= node_regexp_file.read()
	node_static_content		= node_static_file.read()
	php_db_content			= php_db_file.read()
	php_regexp_content		= php_regexp_file.read()
	php_static_content		= php_static_file.read()
	
	# print("File content loaded.")
	
	node_db_bandwidthMatchGroup		= re.search(regexp_bandwidth, node_db_content)
	node_regexp_bandwidthMatchGroup	= re.search(regexp_bandwidth, node_regexp_content)
	node_static_bandwidthMatchGroup	= re.search(regexp_bandwidth, node_static_content)
	php_db_bandwidthMatchGroup		= re.search(regexp_bandwidth, php_db_content)
	php_regexp_bandwidthMatchGroup	= re.search(regexp_bandwidth, php_regexp_content)
	php_static_bandwidthMatchGroup	= re.search(regexp_bandwidth, php_static_content)
	
	node_db_bandwidths.append(float(node_db_bandwidthMatchGroup.group(0)))
	node_regexp_bandwidths.append(float(node_regexp_bandwidthMatchGroup.group(0)))
	node_static_bandwidths.append(float(node_static_bandwidthMatchGroup.group(0)))
	php_db_bandwidths.append(float(php_db_bandwidthMatchGroup.group(0)))
	php_regexp_bandwidths.append(float(php_regexp_bandwidthMatchGroup.group(0)))
	php_static_bandwidths.append(float(php_static_bandwidthMatchGroup.group(0)))
	
	node_db_concurrentMeanMatchGroup		= re.search(regexp_concurrentMean, node_db_content)
	node_regexp_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, node_regexp_content)
	node_static_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, node_static_content)
	php_db_concurrentMeanMatchGroup		= re.search(regexp_concurrentMean, php_db_content)
	php_regexp_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, php_regexp_content)
	php_static_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, php_static_content)
	
	node_db_concurrentMeans.append(float(node_db_concurrentMeanMatchGroup.group(0)))
	node_regexp_concurrentMeans.append(float(node_regexp_concurrentMeanMatchGroup.group(0)))
	node_static_concurrentMeans.append(float(node_static_concurrentMeanMatchGroup.group(0)))
	php_db_concurrentMeans.append(float(php_db_concurrentMeanMatchGroup.group(0)))
	php_regexp_concurrentMeans.append(float(php_regexp_concurrentMeanMatchGroup.group(0)))
	php_static_concurrentMeans.append(float(php_static_concurrentMeanMatchGroup.group(0)))
	
	node_db_meanMatchGroup		= re.search(regexp_mean, node_db_content)
	node_regexp_meanMatchGroup	= re.search(regexp_mean, node_regexp_content)
	node_static_meanMatchGroup	= re.search(regexp_mean, node_static_content)
	php_db_meanMatchGroup		= re.search(regexp_mean, php_db_content)
	php_regexp_meanMatchGroup	= re.search(regexp_mean, php_regexp_content)
	php_static_meanMatchGroup	= re.search(regexp_mean, php_static_content)
	
	node_db_means.append(float(node_db_meanMatchGroup.group(0)))
	node_regexp_means.append(float(node_regexp_meanMatchGroup.group(0)))
	node_static_means.append(float(node_static_meanMatchGroup.group(0)))
	php_db_means.append(float(php_db_meanMatchGroup.group(0)))
	php_regexp_means.append(float(php_regexp_meanMatchGroup.group(0)))
	php_static_means.append(float(php_static_meanMatchGroup.group(0)))
	
	node_db_longestMatchGroup		= re.search(regexp_longest, node_db_content)
	node_regexp_longestMatchGroup	= re.search(regexp_longest, node_regexp_content)
	node_static_longestMatchGroup	= re.search(regexp_longest, node_static_content)
	php_db_longestMatchGroup		= re.search(regexp_longest, php_db_content)
	php_regexp_longestMatchGroup	= re.search(regexp_longest, php_regexp_content)
	php_static_longestMatchGroup	= re.search(regexp_longest, php_static_content)
	
	node_db_longests.append(float(node_db_longestMatchGroup.group(0)))
	node_regexp_longests.append(float(node_regexp_longestMatchGroup.group(0)))
	node_static_longests.append(float(node_static_longestMatchGroup.group(0)))
	php_db_longests.append(float(php_db_longestMatchGroup.group(0)))
	php_regexp_longests.append(float(php_regexp_longestMatchGroup.group(0)))
	php_static_longests.append(float(php_static_longestMatchGroup.group(0)))

#print("")
#print("bandwidths: " + str(bandwidths))
#print("concurrentMeans: " + str(concurrentMeans))
#print("means: " + str(means))
#print("longests: " + str(longests))

node_db_bandwidthTotal = 0
node_regexp_bandwidthTotal = 0
node_static_bandwidthTotal = 0
php_db_bandwidthTotal = 0
php_regexp_bandwidthTotal = 0
php_static_bandwidthTotal = 0

node_db_concurrentMeanTotal = 0
node_regexp_concurrentMeanTotal = 0
node_static_concurrentMeanTotal = 0
php_db_concurrentMeanTotal = 0
php_regexp_concurrentMeanTotal = 0
php_static_concurrentMeanTotal = 0

node_db_meanTotal = 0
node_regexp_meanTotal = 0
node_static_meanTotal = 0
php_db_meanTotal = 0
php_regexp_meanTotal = 0
php_static_meanTotal = 0

node_db_longestTotal = 0
node_regexp_longestTotal = 0
node_static_longestTotal = 0
php_db_longestTotal = 0
php_regexp_longestTotal = 0
php_static_longestTotal = 0

for i in range(0, howmany):
	node_db_bandwidthTotal		+= node_db_bandwidths[i]
	node_regexp_bandwidthTotal	+= node_regexp_bandwidths[i]
	node_static_bandwidthTotal	+= node_static_bandwidths[i]
	php_db_bandwidthTotal		+= php_db_bandwidths[i]
	php_regexp_bandwidthTotal	+= php_regexp_bandwidths[i]
	php_static_bandwidthTotal	+= php_static_bandwidths[i]
	
	node_db_concurrentMeanTotal		+= node_db_concurrentMeans[i]
	node_regexp_concurrentMeanTotal	+= node_regexp_concurrentMeans[i]
	node_static_concurrentMeanTotal	+= node_static_concurrentMeans[i]
	php_db_concurrentMeanTotal		+= php_db_concurrentMeans[i]
	php_regexp_concurrentMeanTotal	+= php_regexp_concurrentMeans[i]
	php_static_concurrentMeanTotal	+= php_static_concurrentMeans[i]
	
	node_db_meanTotal		+= node_db_means[i]
	node_regexp_meanTotal	+= node_regexp_means[i]
	node_static_meanTotal	+= node_static_means[i]
	php_db_meanTotal		+= php_db_means[i]
	php_regexp_meanTotal	+= php_regexp_means[i]
	php_static_meanTotal	+= php_static_means[i]
	
	node_db_longestTotal		+= node_db_longests[i]
	node_regexp_longestTotal	+= node_regexp_longests[i]
	node_static_longestTotal	+= node_static_longests[i]
	php_db_longestTotal			+= php_db_longests[i]
	php_regexp_longestTotal		+= php_regexp_longests[i]
	php_static_longestTotal		+= php_static_longests[i]

node_db_finalBandwidth		= node_db_bandwidthTotal / howmany
node_regexp_finalBandwidth	= node_regexp_bandwidthTotal / howmany
node_static_finalBandwidth	= node_static_bandwidthTotal / howmany
php_db_finalBandwidth		= php_db_bandwidthTotal / howmany
php_regexp_finalBandwidth	= php_regexp_bandwidthTotal / howmany
php_static_finalBandwidth	= php_static_bandwidthTotal / howmany

node_db_finalConcurrentMean		= node_db_concurrentMeanTotal / howmany
node_regexp_finalConcurrentMean	= node_regexp_concurrentMeanTotal / howmany
node_static_finalConcurrentMean	= node_static_concurrentMeanTotal / howmany
php_db_finalConcurrentMean		= php_db_concurrentMeanTotal / howmany
php_regexp_finalConcurrentMean	= php_regexp_concurrentMeanTotal / howmany
php_static_finalConcurrentMean	= php_static_concurrentMeanTotal / howmany

node_db_finalMean		= node_db_meanTotal / howmany
node_regexp_finalMean	= node_regexp_meanTotal / howmany
node_static_finalMean	= node_static_meanTotal / howmany
php_db_finalMean		= php_db_meanTotal / howmany
php_regexp_finalMean	= php_regexp_meanTotal / howmany
php_static_finalMean	= php_static_meanTotal / howmany

node_db_finalLongest		= node_db_longestTotal / howmany
node_regexp_finalLongest	= node_regexp_longestTotal / howmany
node_static_finalLongest	= node_static_longestTotal / howmany
php_db_finalLongest			= php_db_longestTotal / howmany
php_regexp_finalLongest		= php_regexp_longestTotal / howmany
php_static_finalLongest		= php_static_longestTotal / howmany

print("Request type,Node.js,Apache/PHP")

print("Database bandwidth," + str(node_db_finalBandwidth) + "," + str(php_db_finalBandwidth))
print("Database concurrent mean," + str(node_db_finalConcurrentMean) + "," + str(php_db_finalConcurrentMean))
print("Database mean," + str(node_db_finalMean) + "," + str(php_db_finalMean))
print("Database longest," + str(node_db_finalLongest) + "," + str(php_db_finalLongest))

print("String search bandwidth," + str(node_regexp_finalBandwidth) + "," + str(php_regexp_finalBandwidth))
print("String search concurrent mean," + str(node_regexp_finalConcurrentMean) + "," + str(php_regexp_finalConcurrentMean))
print("String search mean," + str(node_regexp_finalMean) + "," + str(php_regexp_finalMean))
print("String search longest," + str(node_regexp_finalLongest) + "," + str(php_regexp_finalLongest))

print("Static file bandwidth," + str(node_static_finalBandwidth) + "," + str(php_static_finalBandwidth))
print("Static file concurrent mean," + str(node_static_finalConcurrentMean) + "," + str(php_static_finalConcurrentMean))
print("Static file mean," + str(node_static_finalMean) + "," + str(php_static_finalMean))
print("Static file longest," + str(node_static_finalLongest) + "," + str(php_static_finalLongest))