import os
import signal
import time

a = os.fork()
if a == 0:
  print "child"
  floc = os.getcwd() + "/chld.py"
  os.execl("/usr/bin/python", "/usr/bin/python", "chld.py")
else:
  print "Parent", a
  time.sleep(5)
  os.kill(a, signal.SIGKILL)
