import os
import sys

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]

phpcommand = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r http://myapp.com/" + name + ".php > c:\\abres\\php_" + num + "-" + con + "-" + name + ".txt"
nodecommand = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r http://myapp.com:3000/" + name + "/ > c:\\abres\\node_" + num + "-" + con + "-" + name + ".txt"

os.system(phpcommand)
os.system(nodecommand)