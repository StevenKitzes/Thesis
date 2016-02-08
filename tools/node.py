import os
import sys

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]
command = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r http://myapp.com:3000/" + name + "/ > c:\\abres\\node_" + num + "-" + con + "-" + name + ".txt"

os.system(command)

print("args found:")
for arg in sys.argv:
	print(arg)
print("Apache command was:")
print(command)