from collections import namedtuple
node=namedtuple('node','name ip port')
with open('conf') as f:
  d=dict()
  nodes=[]
  for line in f:
    line=line.rstrip()
    if not line:
      nodes.append(node(**d))
      d=dict()
    else:
      k,v=line.split(':')
      d[k]=v
  nodes.append(node(**d))
  print nodes
