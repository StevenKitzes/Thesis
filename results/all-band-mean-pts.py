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
regexp_longest = "(?<=(\s))[0-9][\.\d]*(?=(\s\(longest))"

line = "File,node db band,node reg band,node stat band,php db band,php reg band,php stat band,node db mean,node reg mean,node stat mean,php db mean,php reg mean,php stat mean"
print(line)

for i in range(0, howmany):
	line = str(i) + ","
	
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
	
	line += node_db_bandwidthMatchGroup.group(0) + ","
	line += node_regexp_bandwidthMatchGroup.group(0) + ","
	line += node_static_bandwidthMatchGroup.group(0) + ","
	line += php_db_bandwidthMatchGroup.group(0) + ","
	line += php_regexp_bandwidthMatchGroup.group(0) + ","
	line += php_static_bandwidthMatchGroup.group(0) + ","
	
	node_db_concurrentMeanMatchGroup		= re.search(regexp_concurrentMean, node_db_content)
	node_regexp_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, node_regexp_content)
	node_static_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, node_static_content)
	php_db_concurrentMeanMatchGroup		= re.search(regexp_concurrentMean, php_db_content)
	php_regexp_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, php_regexp_content)
	php_static_concurrentMeanMatchGroup	= re.search(regexp_concurrentMean, php_static_content)
	
	line += node_db_concurrentMeanMatchGroup.group(0) + ","
	line += node_regexp_concurrentMeanMatchGroup.group(0) + ","
	line += node_static_concurrentMeanMatchGroup.group(0) + ","
	line += php_db_concurrentMeanMatchGroup.group(0) + ","
	line += php_regexp_concurrentMeanMatchGroup.group(0) + ","
	line += php_static_concurrentMeanMatchGroup.group(0)
	
	print(line)