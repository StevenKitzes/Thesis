import os
import sys

num = sys.argv[1]
name = sys.argv[2]
maxCon = int(sys.argv[3])

currentCon = 2

while currentCon < maxCon:
	command = "python both.py " + num + " " + currentCon + " " + name + " " + str(5)
	os.system(command)
	currentCon = 2 * currentCon