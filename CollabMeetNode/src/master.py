import threading
import instance
import time
import sys
import network
import urllib2

class MasterThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon = True
    self.start()
    
  def run(self):
    while not instance.has_exited:
      time.sleep(instance.HEARTBEAT_SECS)
      if instance.is_master:
        instance.gmutex.acquire()
        send_heartbeats()
        instance.gmutex.release()


def gen_heartbeat_str():
  data = "node:heartbeat:" + str(len(instance.nodes))
  for node in instance.nodes:
    data += ":" + node.name + "#" + node.password + "#" + node.ip + "#" + node.port
  return data


def send_heartbeats():
  data = gen_heartbeat_str()
  print "Sending heartbeats..", data
  for peer in network.get_connection_list():
    if peer not in instance.heartbeat_time:
      instance.heartbeat_time[peer] = time.time()
    if (time.time() - instance.heartbeat_time[peer]) >= instance.HEARTBEAT_TIMEOUT:
      print "Timeout: ", peer, "Current time: ", time.time(), "Last replied: ", instance.heartbeat_time[peer]
      #TODO: handle timeout
    else:
      network.send(peer, data)
  print "Heartbeat reply times:", instance.heartbeat_time


def init_master():
  print "Initializing master..."
  for index, node in enumerate(instance.nodes):
    if node.name == instance.name:
      instance.nodes[index] = instance.nodes[index]._replace(ip = instance.local_ip)
      instance.nodes[index] = instance.nodes[index]._replace(port = str(instance.listen_port))
  instance.is_master = True
  try:
    url = "http://ec2-50-112-192-196.us-west-2.compute.amazonaws.com:1337/insert?id=" + str(instance.meeting_id)
    url += "&ip=" + instance.name + ":" + instance.local_ip + ":" + str(instance.listen_port)
    data = urllib2.urlopen(url).read() #blocking
    if data != "Inserted!\n":
      sys.exit(1)
  except:
    print "Error! Cannot connect to bootstrap server!"
    sys.exit(1)
  send_heartbeats()
   
   
# Master Message Handling

def handle_join(strs, sock):
  for index, node in enumerate(instance.nodes):
    if node.name == strs[instance.SENDER] and node.password == strs[3]:
      if strs[4] != 'Mobile':
        instance.nodes[index] = instance.nodes[index]._replace(ip = strs[4])
        instance.nodes[index] = instance.nodes[index]._replace(port = strs[5])
        data = gen_heartbeat_str()
        sock.sendall(instance.name + ":" + data)
        send_heartbeats() # inform others
      else:
        data = gen_heartbeat_str()
        sock.sendall(instance.name + ":" + data + "\n")
      return
  reply = "node:joinreject"
  print "Join rejected!"
  if strs[4] != "Mobile":
    sock.sendall(instance.name + ":" + reply)
  else:
    sock.sendall(instance.name + ":" + reply + "\n")


def handle_heartbeatreply(strs, sock):
  instance.heartbeat_time[strs[instance.SENDER]] = time.time()

 
def handle_message(data, sock):
  strs = data.split(':')
  if not instance.is_master:
    return
  if strs[instance.MSGTYPE] == 'join':
    handle_join(strs, sock)
  elif strs[instance.MSGTYPE] == 'heartbeatreply':  
    handle_heartbeatreply(strs, sock)
  else:
    print 'Error! Invalid message to master'