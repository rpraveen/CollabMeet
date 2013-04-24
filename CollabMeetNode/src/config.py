from collections import namedtuple
import instance

Node = namedtuple('Node','name password ip port')

def parse():
  """Read configuration file into nodes"""
  try:
    with open(instance.name) as f:
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
      instance.curr_master = instance.name
  except:
    pass
  
def get_node_index(name):
  for index, node in enumerate(instance.nodes):
    if node.name == name:
      return index
  return 0