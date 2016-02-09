import os
import sys

if sys.argv[1]:
	if sys.argv[1] == "-h":
		print("Expected arguments are all mandatory and must appear in order.")
		print("")
		print("    python series-it.py [num] [name] [maxCon] [desiredIterations]")
		print("")
		print("[num]                    - how many requests to make per series")
		print("[name]                   - name of the test that will be run")
		print("[maxCon]                 - concurrency level starts at two and")
		print("                           increases by powers of two until this")
		print("                           value is reached")
		print("[desiredIterations       - how many times to run the same test in")
		print("                           the series (to investigate consistency)")
		sys.exit()

num = sys.argv[1]
name = sys.argv[2]
maxCon = int(sys.argv[3])
desiredIterations = sys.argv[4]

currentCon = 2

while currentCon < maxCon:
	command = "python series.py " + num + " " + str(currentCon) + " " + name + " " + desiredIterations
	os.system(command)
	currentCon = 2 * currentCon