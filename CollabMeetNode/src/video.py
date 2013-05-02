import instance
import os
import sys
import signal

def create_server():
	if instance.VIDEO_ENABLED == False:
		return
	instance.child_pid = os.fork()
	if instance.child_pid == 0:
		print "Creating video server.."
		print instance.curr_video_name + ":" + instance.curr_video_ip + ":" + str(instance.curr_video_port)
  		os.execl("/usr/bin/python", "/usr/bin/python", "fs-gui.py", "s", str(instance.curr_video_port). instance.camera)
  		sys.exit(1)

def stop_server():
	if instance.child_pid != 0:
		os.kill(instance.child_pid, signal.SIGKILL)

def create_client():
	if instance.VIDEO_ENABLED == False:
		return
	instance.child_pid = os.fork()
	if instance.child_pid == 0:
		print "Creating video client.."
		print instance.curr_video_name + ":" + instance.curr_video_ip + ":" + str(instance.curr_video_port)
  		os.execl("/usr/bin/python", "/usr/bin/python", "fs-gui.py", "c", instance.curr_video_ip, str(instance.curr_video_port), instance.camera)
  		sys.exit(1)

def stop_client():
	if instance.child_pid != 0:
		os.kill(instance.child_pid, signal.SIGKILL)
  