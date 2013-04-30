import network
import instance
import master
import p1
  
""" APIs for GUI integration """

def init_gui():
  p1.markui1()
  pass


def send_text_msg(text):
  msg = "node:textmsg:" + text
  instance.gmutex.acquire()
  for peer in network.get_connection_list():
    if peer == instance.name:
      continue;
    network.send(peer, msg)
  instance.gmutex.release()


def received_text_msg(sender, text):
  print "Text message: sender:" + sender + " text:" + text
  p1.print_data(sender, text)
  pass


def update_map_loc(name, latitude, longitude):
  print "Mobile location update: sender:" + name + " latitude:" + latitude + " longitude:" + longitude
  #TODO: update GUI
  pass


""" APIs for video multicasting """

def init_video_module():
  #TODO: init module
  pass


def send_video_req():
  instance.gmutex.acquire()
  if instance.is_master:
    msg = instance.name + ":master:videoreq:" + instance.local_ip + ":" + str(instance.video_port)
    master.handle_message(msg, None)
  else:
    msg = "master:videoreq:" + instance.local_ip + ":" + str(instance.video_port)
    network.send(instance.curr_master, msg)
  instance.gmutex.release()


def send_video_stop_req():
  instance.gmutex.acquire()
  if instance.is_master:
    msg = instance.name + ":master:videostop"
    master.handle_message(msg, None)
  else:
    msg = "master:videostop"
    network.send(instance.curr_master, msg)
  instance.gmutex.release()
  

def start_video_stream():
  #TODO: start streaming video
  pass


def stop_video_stream():
  #TODO: stop streaming video
  pass


def connect_to_video_server(name, ip, port):
  #TODO: connect to server
  pass

def disconnect_video_server():
  #TODO: disconnect server
  pass


def update_video_source(name, ip, port):
  print "Video source: name:" + name + " ip:" + ip + " port:" + str(port)
  if instance.initialized == True:
    if instance.curr_video_name == name:
      # Ignore this update
      return
    if instance.curr_video_name == instance.name:
      # Server. So stop streaming
      stop_video_stream()
    else:
      # Client. Disconnect from server
      disconnect_video_server()
    if name == instance.name:
      start_video_stream()
    else:
      connect_to_video_server(name, ip, port)
  instance.curr_video_name = name
  instance.curr_video_ip = ip
  instance.curr_video_port = port
