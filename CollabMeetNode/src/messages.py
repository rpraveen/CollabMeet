import instance
import config
import network
import sys
import master
import time
import api

def handle_heartbeat(strs):
  instance.last_heartbeat_rcvd = time.time()
  if instance.is_master and instance.name != strs[instance.SENDER]:
    master.clear_master()
  instance.curr_master = strs[instance.SENDER]
  instance.nodes = []
  nodecount = int(strs[instance.NODECOUNT])
  for i in range(4, 4 + nodecount):
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
  video_name = strs[4 + nodecount]
  video_ip = strs[5 + nodecount]
  video_port = int(strs[6 + nodecount])
  api.update_video_source(video_name, video_ip, video_port)
  
    
def handle_message(data):
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
    api.update_map_loc(sender, latitude, longitude)
  elif strs[instance.MSGTYPE] == 'textmsg':
    sender = strs[instance.SENDER]
    text = strs[3]
    api.received_text_msg(sender, text)
  else:
    print 'Error! Invalid message'