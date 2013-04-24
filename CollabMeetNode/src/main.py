import sys
import socket
import network
import config
import instance
import master
import time

############
#   main   #
############

def main():  
  if len(sys.argv) != 3: 
    print '<usage> name port'
    sys.exit(1)
  
  instance.name = sys.argv[1]
  #instance.local_ip = '127.0.0.1'
  instance.local_ip = '192.168.0.104'
  instance.listen_port = int(sys.argv[2])
  
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
      #TODO: error check
      
      instance.gmutex.acquire()
      if commands[0] == 's':
        network.send(commands[1],commands[2])
      elif command[0] == 'q':
        instance.has_exited = True
        network.close_connections()
        sys.exit(0)
      else:
        print 'This command is not supported'
      instance.gmutex.release()
    except KeyboardInterrupt:
      sys.exit(1)

if __name__ == "__main__":
    main()