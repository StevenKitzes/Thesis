import os
import sys

server = "http://192.168.0.10/"

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]

args = len(sys.argv)
mod = ""
if args > 4:
	mod = "_" + sys.argv[4]

print("")
print("Running Apache/PHP test [" + name + "] with " + num + " requests, and " + con + " concurrency.")
if args > 4:
	print("(Iteration: " + str((int(sys.argv[4]) + 1)) + ")")

resource = server

if name == 'static':
	resource += "static.jpg"
elif name == 'simpleStatic':
	resource += "simpleStatic.jpg"
else:
	resource += name + ".php"

command = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r -l -s 999999 " + resource + " > ..\\results\\php_" + num + "-" + con + "-" + name + mod + ".txt"

os.system(command)