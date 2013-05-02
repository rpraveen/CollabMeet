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
import master
import messages
import urllib2
import os
import gui

connection_list = dict()

class Receiver(threading.Thread):
  def __init__(self,client_socket):
    threading.Thread.__init__(self)
    self.daemon=True
    self.cs=client_socket
    self.start()

  def run(self):
    while not instance.has_exited:
      data = self.cs.recv(1024) #blocking
      if not data:  
        break
      #print '[recv]', data
      strs = data.split(':')
      
      instance.gmutex.acquire()
      if strs[instance.MODULE] == 'master':
        master.handle_message(data, self.cs)
      else:
        messages.handle_message(data)
      instance.gmutex.release()
    self.cs.close()


class ListeningThread(threading.Thread):
  def __init__(self,sock):
    threading.Thread.__init__(self)
    self.daemon = True
    self.sock=sock
    self.start()
    
  def run(self):
    try:
      self.sock.bind(('0.0.0.0', instance.listen_port))
      self.sock.listen(5) #blocking
    except:
      print "Error! Cannot bind to address! Retry with different port!"
      os._exit(1)

    while not instance.has_exited:
      try:
        conn, addr = self.sock.accept()
        #print '[Connected by', addr, ']'
        Receiver(conn)
      except:
        sys.exit(1)


class ConnectingThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon = True
    self.start()

  def run(self):
    global connection_list
    while not instance.has_exited:
      for node in instance.nodes:
        if node.name == instance.name:
          continue
        if node.port == '0':
          continue
        dest_name = node.name
        host = node.ip
        port = int(node.port) 
        if dest_name not in connection_list:
          print '[try to connect to', dest_name, '...]'
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          try:
            s.connect((host, port)) #blocking
            instance.gmutex.acquire() 
            connection_list[dest_name]=s
            gui.update_meeting_info()
            instance.gmutex.release()
            print '[Connected!]', dest_name
          except:
            print 'Exception! Cannot connect to', dest_name
            time.sleep(1)
            pass
      time.sleep(instance.CONN_RETRY_SECS)
    #TODO: handle broken conn and update group info  

def send(dst, data):
  global connection_list
  msg = instance.name + ":" + data
  #print '[send]', msg
  if dst in connection_list:
    try:
      s = connection_list[dst]
      s.sendall(msg)
    except:
      print "Connection error!"
      remove_peer(dst)
  else:
    print "Error sending message!", dst, "not in connection list!"
  
  
def get_connection_list():
  global connection_list
  connlist = []
  for peer in connection_list:
    connlist.append(peer)
  return connlist


def close_connections():
  global connection_list
  for peer in connection_list:
    connection_list[peer].close()


def remove_peer(name):
  if instance.initialized == False:
    return
  global connection_list
  if name in connection_list:
    print "## Removing peer: " + name
    del connection_list[name]
  if name in instance.heartbeat_time:
    del instance.heartbeat_time[name]
  for index, node in enumerate(instance.nodes):
    if node.name == name:
      instance.nodes[index] = instance.nodes[index]._replace(ip = '0.0.0.0')
      instance.nodes[index] = instance.nodes[index]._replace(port = '0')
      break
  gui.update_meeting_info()


def join_meeting():
  try:
    url = "http://ec2-50-112-192-196.us-west-2.compute.amazonaws.com:1337/lookup?id=" + str(instance.meeting_id)
    data = urllib2.urlopen(url).read()  #blocking (with only 1 thread)
    strs = data.split(':')
    print "Contacting master (" + strs[0] + ")..."
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((strs[1], int(strs[2])))  #blocking (with only 1 thread)
    connection_list[strs[0]] = sock
    send(strs[0], "master:join:" + instance.password + ":" + instance.local_ip + ":" + str(instance.listen_port))
    data = sock.recv(4096)
    messages.handle_message(data)
  except:
    print "Error! Cannot connect to meeting!"
    sys.exit(1)
