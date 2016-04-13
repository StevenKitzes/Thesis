import subprocess

def n_fireSimple():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10000","-c","64","http://192.168.0.10:3000/db/",">","n_simple.txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def n_fireRegexp():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10","-c","1","http://192.168.0.10:3000/regexp/",">","n_regexp.txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def n_fireStatic():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10","-c","1","http://192.168.0.10:3000/reactor.jpg",">","n_static.txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def p_fireSimple():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10000","-c","64","http://192.168.0.10/db.php",">","p_simple.txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def p_fireRegexp():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10","-c","1","http://192.168.0.10/regexp.php",">","p_regexp.txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def p_fireStatic():
	subprocess.Popen(["c:/apache24/bin/ab.exe", "-n","10","-c","1","http://192.168.0.10/reactor.jpg",">","p_static.txt"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

p_fireStatic()
p_fireSimple()
p_fireRegexp()