import subprocess
import sys

def showUsage():
	print("Usage guidelines for this script:")
	print("")
	print("Args:")
	print("1 - must be in [\"node\", \"php\"]")
	print("2 - [optional] file name modifier")
	sys.exit()

mod = ""
which = ""

if len(sys.argv) < 2:
	showUsage()
if sys.argv[1] != "node" and sys.argv[1] != "php":
	showUsage()
else:
	which = sys.argv[1]

if len(sys.argv) > 2:
	mod = "_" + sys.argv[2]

def n_fireDatabase():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10000","-c","64","http://192.168.29.236:3000/db/",">","../results/n_database" + mod + ".txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def n_fireRegexp():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","30","-c","1","http://192.168.29.236:3000/regexpChildPing/",">","../results/n_regexp" + mod + ".txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def n_fireStatic():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","30","-c","1","http://192.168.29.236:3000/reactor.jpg",">","../results/n_static" + mod + ".txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def p_fireDatabase():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10000","-c","64","http://192.168.29.236/db.php",">","../results/p_database" + mod + ".txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def p_fireRegexp():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","30","-c","1","http://192.168.29.236/regexpChildPing.php",">","../results/p_regexp" + mod + ".txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def p_fireStatic():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","30","-c","1","http://192.168.29.236/reactor.jpg",">","../results/p_static" + mod + ".txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

if which == "node":
	n_fireStatic()
	n_fireDatabase()
	n_fireRegexp()
elif which == "php":
	p_fireStatic()
	p_fireDatabase()
	p_fireRegexp()
else:
	showUsage()