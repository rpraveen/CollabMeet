import instance
import config
import network
import sys
import master
import time

def handle_heartbeat(strs):
  instance.last_heartbeat_rcvd = time.time()
  instance.curr_master = strs[instance.SENDER]
  if instance.is_master:
    master.clear_master()
  instance.nodes = []
  for i in range(4, 4 + int(strs[instance.NODECOUNT])):
    s = strs[i]
    val = s.split('#')
    d = dict()
    d['name'] = val[0]
    d['password'] = val[1]
    d['ip'] = val[2]
    d['port'] = val[3]
    instance.nodes.append(config.Node(**d))
  reply = "master:heartbeatreply"
  network.send(instance.curr_master, reply)
  
    
def handle_message(data, sock):
  strs = data.split(':')
  if strs[instance.MSGTYPE] == 'heartbeat':
    handle_heartbeat(strs)
  elif strs[instance.MSGTYPE] == 'joinreject':
    print 'Error! Join rejected'
    sys.exit(1)
  elif strs[instance.MSGTYPE] == 'mobilelocation':
    sender = strs[instance.SENDER]
    latitude = strs[3]
    longitude = strs[4]
    #print "Mobile location update: sender:" + sender + " latitude:" + latitude + " longitude:" + longitude
  else:
    print 'Error! Invalid message'