import sys
import socket
import network
import config
import instance

############
#   main   #
############

def main():  
  if len(sys.argv) != 2: 
    print '<usage> name'
    sys.exit(1)
  
  instance.name = sys.argv[1]
  
  config.parse()
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  network.ListeningThread(s)
  network.ConnectingThread()
  
  while 1:
    try:
      command = raw_input('>>> s for send(s:destination_ip:string); q for exit\n')
      if len(command) == 0:
        continue
      commands=command.split(':')
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