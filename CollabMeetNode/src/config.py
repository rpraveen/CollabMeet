from collections import namedtuple
import instance

Node = namedtuple('Node','name ip port')

def parse():
  """Read configuration file into nodes"""
  with open('conf') as f:
    d=dict()
    for line in f:
      line=line.rstrip()
      if not line:
        instance.nodes.append(Node(**d))
        d=dict()
      else:
        k,v=line.split(':')
        d[k]=v
    instance.nodes.append(Node(**d))
    
    for node in instance.nodes:
      if node.name == instance.name:
        instance.local_ip = node.ip
        instance.listen_port = int(node.port)