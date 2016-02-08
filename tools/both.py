import os
import sys

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]

args = len(sys.argv)
mod = ""
if args > 4:
	mod = " " + sys.argv[4]

phpcommand = "python php.py " + num + " " + con + " " + name + mod
nodecommand = "python node.py " + num + " " + con + " " + name + mod

os.system(phpcommand)
os.system(nodecommand)