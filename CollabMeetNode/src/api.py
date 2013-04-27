import network
import instance
import master
  
""" APIs for GUI integration """

def init_gui():
  #TODO: init GUI
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
  #TODO: update GUI
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
    msg = instance.name + ":master:videoreq:" + str(instance.video_port)
    master.handle_message(msg, None)
  else:
    msg = "master:videoreq:" + str(instance.video_port)
    network.send(instance.curr_master, msg)
  instance.gmutex.release()


def ready_for_video():
  #TODO: start streaming video
  pass


def stop_video():
  #TODO: stop streaming video
  pass


def connect_to_video_server(name, ip, port):
  #TODO: connect to server
  pass


def update_video_source(isStreaming, name, ip, port):
  pass