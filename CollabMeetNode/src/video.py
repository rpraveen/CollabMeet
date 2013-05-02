import instance
import os
import sys
import signal

def create_server():
	instance.child_pid = os.fork()
	if instance.child_pid == 0:
		print "Creating video server.."
		print instance.curr_video_name + ":" + instance.curr_video_ip + ":" + str(instance.curr_video_port)
  		os.execl("/usr/bin/python", "/usr/bin/python", "chld_server.py")
  		sys.exit(1)

def stop_server():
	if instance.child_pid != 0:
		os.kill(instance.child_pid, signal.SIGKILL)

def create_client():
	instance.child_pid = os.fork()
	if instance.child_pid == 0:
		print "Creating video client.."
		print instance.curr_video_name + ":" + instance.curr_video_ip + ":" + str(instance.curr_video_port)
  		os.execl("/usr/bin/python", "/usr/bin/python", "chld_client.py")
  		sys.exit(1)

def stop_client():
	if instance.child_pid != 0:
		os.kill(instance.child_pid, signal.SIGKILL)
  