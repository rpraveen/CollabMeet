import sys
import socket
import network
import config
import instance
import master
import time
import api

############
#   main   #
############

def main():  
  if len(sys.argv) != 5: 
    print '<usage> name ip port videoport'
    sys.exit(1)
  
  instance.name = sys.argv[1]
  instance.local_ip = sys.argv[2]
  instance.listen_port = int(sys.argv[3])
  instance.video_port = int(sys.argv[3])
  
  instance.local_ip = '128.237.130.30'
  
  config.parse()
  
  if instance.curr_master == instance.name:
    master.init_master()
  else:
    network.join_meeting()
  
  instance.last_heartbeat_rcvd = time.time()
  instance.master_thread = master.MasterThread()
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  network.ListeningThread(s)
  network.ConnectingThread()
  
  while 1:
    try:
      command = raw_input()
      if len(command) == 0:
        continue
      commands = command.split(':')
      if commands[0] == 'q':
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