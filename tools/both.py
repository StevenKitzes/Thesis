import os
import sys

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]

args = len(sys.argv)
mod = ""
if(args > 4):
	mod = "_" + sys.argv[4]

phpcommand = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r http://myapp.com/" + name + ".php > c:\\abres\\php_" + num + "-" + con + "-" + name + mod + ".txt"
nodecommand = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r http://myapp.com:3000/" + name + "/ > c:\\abres\\node_" + num + "-" + con + "-" + name + mod + ".txt"

os.system(phpcommand)
os.system(nodecommand)