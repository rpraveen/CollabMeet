import threading
import instance
import time
import sys
import network
import urllib2
import config
import api

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
      else:
        node_index = config.get_node_index(instance.name)
        master_index = config.get_node_index(instance.curr_master)
        if node_index == master_index:
          continue
        elif node_index > master_index:
          timeout_val = (node_index - master_index) * instance.HEARTBEAT_TIMEOUT
        else:
          timeout_val = (len(instance.nodes) + node_index - master_index) * instance.HEARTBEAT_TIMEOUT
        #print "Master timeout val:", timeout_val
        if (time.time() - instance.last_heartbeat_rcvd) >= timeout_val:
          init_master()


def gen_heartbeat_str():
  data = "node:heartbeat:" + str(len(instance.nodes))
  for node in instance.nodes:
    data += ":" + node.name + "#" + node.password + "#" + node.ip + "#" + node.port
  data += ":" + instance.curr_video_name + ":" + instance.curr_video_ip + ":" + str(instance.curr_video_port)
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
  #print "Heartbeat reply times:", instance.heartbeat_time
  api.update_video_source(instance.curr_video_name, instance.curr_video_ip, instance.curr_video_port)


def init_master():
  print "Initializing master..."
  for index, node in enumerate(instance.nodes):
    if node.name == instance.name:
      instance.nodes[index] = instance.nodes[index]._replace(ip = instance.local_ip)
      instance.nodes[index] = instance.nodes[index]._replace(port = str(instance.listen_port))
  instance.is_master = True
  instance.curr_master = instance.name
  try:
    url = "http://ec2-50-112-192-196.us-west-2.compute.amazonaws.com:1337/insert?id=" + str(instance.meeting_id)
    url += "&ip=" + instance.name + ":" + instance.local_ip + ":" + str(instance.listen_port)
    data = urllib2.urlopen(url).read() #blocking
    if data != "Inserted!\n":
      sys.exit(1)
  except:
    print "Error! Cannot connect to bootstrap server!"
    sys.exit(1)
  instance.gmutex.acquire()
  send_heartbeats()
  instance.gmutex.release()
  
def clear_master():
  print "Clearing master..."
  instance.is_master = False
  instance.last_heartbeat_rcvd = time.time() 
   
# Master Message Handling

def handle_join(strs, sock):
  for index, node in enumerate(instance.nodes):
    if node.name == strs[instance.SENDER] and node.password == strs[3]:
      if strs[4] != 'Mobile':
        instance.nodes[index] = instance.nodes[index]._replace(ip = strs[4])
        instance.nodes[index] = instance.nodes[index]._replace(port = strs[5])
        data = gen_heartbeat_str()
        data += ":" + instance.chat_msgs
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


def handle_heartbeatreply(strs):
  instance.heartbeat_time[strs[instance.SENDER]] = time.time()

 
def handle_videoreq(strs):
  if instance.curr_video_name != strs[instance.SENDER]:
    #TODO: handle waiting lists
    return
  instance.curr_video_name = strs[instance.SENDER]
  instance.curr_video_ip = strs[3]
  instance.curr_video_port = int(strs[4])


def handle_videostop(strs):
  instance.curr_video_name = 'none'
  instance.curr_video_ip = '0.0.0.0'
  instance.curr_video_port = 0
 
 
def handle_message(data, sock):
  strs = data.split(':')
  if not instance.is_master:
    print "Error! Dropping master packets"
    return
  if strs[instance.MSGTYPE] == 'join':
    handle_join(strs, sock)
  elif strs[instance.MSGTYPE] == 'heartbeatreply':  
    handle_heartbeatreply(strs)
  elif strs[instance.MSGTYPE] == 'videoreq':
    handle_videoreq(strs)
  elif strs[instance.MSGTYPE] == 'videostop':
    handle_videostop(strs)
  else:
    print 'Error! Invalid message to master'
