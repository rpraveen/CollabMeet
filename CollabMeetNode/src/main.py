import sys
import socket
import network
import config
import instance
import master

############
#   main   #
############

def join_meeting():
  pass

def main():  
  if len(sys.argv) != 3: 
    print '<usage> name port'
    sys.exit(1)
  
  instance.name = sys.argv[1]
  instance.local_ip = '127.0.0.1'
  instance.listen_port = int(sys.argv[2])
  
  config.parse()
  
  if instance.curr_master == instance.name:
    instance.master_thread = master.MasterThread()
  else:
    join_meeting()
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  network.ListeningThread(s)
  network.ConnectingThread()
  
  while 1:
    try:
      command = raw_input('>>> s for send(s:destination_ip:string); q for exit\n')
      if len(command) == 0:
        continue
      commands = command.split(':')
      #TODO: error check
      if commands[0] == 's':
        network.send(commands[1],commands[2])
      elif command[0] == 'q': 
        sys.exit(1)
      else:
        print 'This command is not supported'
    except KeyboardInterrupt:
      sys.exit(1)

if __name__ == "__main__":
    main()