## 
# @ file node.py
#
# Each node read configuration file from 'conf' (suppose from bootstrap server)
# for group infomation and establish connection for each pair of node.
# Have a command line UI like lab0 we did
# 
# Author: Ting-An Wang
# Create on 4-1-2013
#

import socket
import sys
import threading
import time
from collections import namedtuple

class Receiver(threading.Thread):
  def __init__(self,client_socket):
    threading.Thread.__init__(self)
    self.daemon=True
    self.cs=client_socket
    self.start()

  def run(self):
    while 1:
      data = self.cs.recv(1024)
      if not data:  
        break
      print '[recv] ', data

    print '[close]'
    self.cs.close()

class ListeningThread(threading.Thread):
  def __init__(self,sock,port):
    threading.Thread.__init__(self)
    self.daemon = True
    self.sock=sock
    self.port=port
    self.start()
    
  def run(self):
    global LOCALIP
    self.sock.bind((LOCALIP,self.port))
    self.sock.listen(5)
    while 1:
      try:
        print '[listening...]'
        conn, addr = self.sock.accept()     #blocking
        print '[Connected by', addr, ']'
        Receiver(conn)
      except KeyboardInterrupt:
        sys.exit(1)


class ConnectingThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon = True
    self.start()

  def run(self):
    """Spawn a thread to connect to each node in the conf list except herself"""
    global SELF
    global connection_list

    while len(connection_list.keys()) != len(nodes)-1: #except self
      #print 'now:',len(connection_list.keys()), ' ls:',len(nodes)-1
      for node in nodes:
        if node.name==SELF:
          continue
        DESTNAME=node.name
        HOST=node.ip
        PORT=int(node.port) 
        if DESTNAME not in connection_list:
          print '[try to connect to', DESTNAME, '...]'
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          try:
            s.connect((HOST,PORT))  
            connection_list[DESTNAME]=s
            print '[Connected!]'
          except:
            time.sleep(1)
            pass

    print '[everyone online :D]'
    #print connection_list
    #TODO: handle broken conn and update group info  

def parse():
  """Read configuration file into nodes"""
  global nodes
  global node
  with open('conf') as f:
    d=dict()
    for line in f:
      line=line.rstrip()
      if not line:
        nodes.append(node(**d))
        d=dict()
      else:
        k,v=line.split(':')
        d[k]=v
    nodes.append(node(**d))
    #print nodes
  for node in nodes:
    if node.name==SELF:
      LOCALIP=node.ip

def send(dst, data):
  global connection_list
  print '[sending', repr(data), 'to ', dst, '...]'
  s=connection_list[dst.lower()]
  s.sendall(data);
  print '[Sent!]'


############
#   main   #
############

node=namedtuple('node','name ip port')
nodes=[]
connection_list=dict()
SELF=''
LISTENINGPORT=0
LOCALIP=''

def main():
  global SELF
  global LISTENINGPORT

  if len(sys.argv)!=3: 
    print '<usage> ip port'
    sys.exit(1)
  
  SELF=sys.argv[1]
  LISTENINGPORT=int(sys.argv[2])
  
  parse()
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ListeningThread(s,LISTENINGPORT)
  ConnectingThread()
  while 1:
    try:
      command = raw_input('>>> s for send(s:destination_ip:string); q for exit\n')
      if len(command)==0:
        continue
      commands=command.split(':')

      #TODO: error check
      if commands[0] == 's':
        send(commands[1],commands[2])
      elif command[0] == 'q': 
        sys.exit(1)
      else:
        print 'This command is not supported'
    except KeyboardInterrupt:
      sys.exit(1)

if __name__ == "__main__":
    main()


