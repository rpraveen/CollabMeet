import threading
import instance
import time
import network

class MasterThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon = True
    self.heartbeat_time = dict()
    self.start()
    
  def run(self):
    instance.is_master = True
    while instance.is_master:
      time.sleep(instance.HEARTBEAT_SECS)
      print "Sending heartbeats..", self.heartbeat_time
      for peer in network.get_connection_list():
        if peer not in self.heartbeat_time:
          self.heartbeat_time[peer] = time.time()
        if (time.time() - self.heartbeat_time[peer]) >= instance.HEARTBEAT_TIMEOUT:
          print "Timeout: ", peer, "Current time: ", time.time(), "Last replied: ", self.heartbeat_time[peer]
  
def handle_data(data):
  pass