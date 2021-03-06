import os
import sys

num = sys.argv[1]
con = sys.argv[2]
name = sys.argv[3]

args = len(sys.argv)
mod = ""
if args > 4:
	mod = "_" + sys.argv[4]

print("")
print("Running Node test [" + name + "] with " + num + " requests, and " + con + " concurrency.")
if args > 4:
	print("(Iteration: " + str((int(sys.argv[4]) + 1)) + ")")

if name == 'static':
	command = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r -l -s 999999 http://192.168.0.10:3000/reactor.jpg > ..\\results\\node_" + num + "-" + con + "-" + name + mod + ".txt"
else:
	command = "c:\\Apache24\\bin\\ab.exe -n " + num + " -c " + con + " -r -l -s 999999 http://192.168.0.10:3000/" + name + "/ > ..\\results\\node_" + num + "-" + con + "-" + name + mod + ".txt"

os.system(command)