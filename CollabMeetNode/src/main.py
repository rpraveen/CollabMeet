#!/usr/bin/env python
import sys
import socket
import network
import config
import instance
import master
import time
import api
import gobject, gtk
import map_decode

gtk.gdk.threads_init()


############
#   main   #
############

def main():  
  if len(sys.argv) < 7: 
    print '<usage> $ %s node_name ip port videoport meetingid mode(c for client, s for server) <path_to_camera>' % sys.argv[0]
    sys.exit(1)
  
  instance.name = sys.argv[1]
  instance.local_ip = sys.argv[2]
  instance.listen_port = int(sys.argv[3])
  instance.video_port = int(sys.argv[4])
  instance.meeting_id = int(sys.argv[5])
  instance.mode = sys.argv[6]
  assert(instance.mode == 'c' or instance.mode == 's')
  instance.camera = None
  if len(sys.argv) == 8:
  	instance.camera = sys.argv[7]

  config.parse()
  
  if instance.curr_master == instance.name:
    master.init_master()
  else:
    network.join_meeting()
  
  instance.initialized = True
  
  instance.last_heartbeat_rcvd = time.time()
  instance.master_thread = master.MasterThread()
  
  if instance.curr_video_port != 0:
    api.connect_to_video_server(instance.curr_video_name, instance.curr_video_ip, instance.curr_video_port)
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  network.ListeningThread(s)
  network.ConnectingThread()
  map_decode.MapThread()

  api.init_gui(instance.mode, instance.local_ip, instance.video_port, instance.camera) # client should know server's ip
  
  while 1:
    try:
      command = raw_input()
      if len(command) == 0:
        continue
      commands = command.split(':')
      if commands[0] == 'q':
        print "Quitting.."
        instance.has_exited = True
        network.close_connections()
        sys.exit(0)
      elif commands[0] == 'text':
        api.send_text_msg(commands[1])
      elif commands[0] == 'video':
        api.send_video_req()
      else:
        print 'This command is not supported'
    except KeyboardInterrupt:
      sys.exit(1)

if __name__ == "__main__":
    main()
