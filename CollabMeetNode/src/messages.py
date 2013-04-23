import instance
import config
import network
import sys

def handle_heartbeat(strs):
  instance.curr_master = strs[instance.SENDER]
  for index, s in enumerate(strs):
    if index < 3:
      continue
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
  else:
    print 'Error! Invalid message'