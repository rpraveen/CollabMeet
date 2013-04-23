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
import instance

connection_list = dict()

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
  def __init__(self,sock):
    threading.Thread.__init__(self)
    self.daemon = True
    self.sock=sock
    self.start()
    
  def run(self):
    self.sock.bind((instance.local_ip, instance.listen_port))
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
    print "Lname: ", instance.name
    """Spawn a thread to connect to each node in the conf list except herself"""
    while len(connection_list.keys()) != (len(instance.nodes) - 1): #except self
      #print 'now:',len(connection_list.keys()), ' ls:',len(nodes)-1
      for node in instance.nodes:
        if node.name == instance.name:
          continue
        dest_name = node.name
        host = node.ip
        port = int(node.port) 
        if dest_name not in connection_list:
          print '[try to connect to', dest_name, '...]'
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          try:
            s.connect((host, port))  
            connection_list[dest_name]=s
            print '[Connected!]'
          except:
            time.sleep(1)
            pass

    print '[everyone online :D]'
    #print connection_list
    #TODO: handle broken conn and update group info  

def send(dst, data):
  global connection_list
  print '[sending', repr(data), 'to ', dst, '...]'
  s = connection_list[dst.lower()]
  s.sendall(data);
  print '[Sent!]'