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

howmany = int(sys.argv[1])

#print("Calculating some averages over " + howmany + " batches")

regexp_bandwidth = "[0-9][\.\d]*(?=(\s\[#))"
regexp_concurrentMean = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean,))"
regexp_mean = "[0-9][\.\d]*(?=(\s\[ms\]\s\(mean\)))"
regexp_longest = "(?<=(\s))[0-9][\.\d]*(?=(\s\(longest request\)))"

line = "File,Node.js bandwidth,Apache/PHP bandwidth,Node.js mean,Apache/PHP mean,Node.js longest,Apache/PHP longest"
print(line)

for i in range(0, howmany):
	line = str(i) + ","
	
	node_db_incomingFile		= "n_database_" + str(i) + ".txt"
	php_db_incomingFile			= "p_database_" + str(i) + ".txt"
	
	node_db_file		= open(node_db_incomingFile)
	php_db_file			= open(php_db_incomingFile)
	
	node_db_content			= node_db_file.read()
	php_db_content			= php_db_file.read()
	
	# print("File content loaded.")
	
	node_db_bandwidthMatchGroup		= re.search(regexp_bandwidth, node_db_content)
	php_db_bandwidthMatchGroup		= re.search(regexp_bandwidth, php_db_content)
	
	line += node_db_bandwidthMatchGroup.group(0) + ","
	line += php_db_bandwidthMatchGroup.group(0) + ","
	
	node_db_meanMatchGroup		= re.search(regexp_mean, node_db_content)
	php_db_meanMatchGroup		= re.search(regexp_mean, php_db_content)
	
	line += node_db_meanMatchGroup.group(0) + ","
	line += php_db_meanMatchGroup.group(0) + ","
	
	node_db_longestMatchGroup		= re.search(regexp_longest, node_db_content)
	php_db_longestMatchGroup		= re.search(regexp_longest, php_db_content)
	
	line += node_db_longestMatchGroup.group(0) + ","
	line += php_db_longestMatchGroup.group(0)
	
	print(line)