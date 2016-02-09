import os
import sys

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]
repeat = sys.argv[4]

for i in range(0, int(repeat)):
	command = "python node.py " + num + " " + con + " " + name + " " + str(i)
	os.system(command)