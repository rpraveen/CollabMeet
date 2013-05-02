import network
import instance
import master
import time
import gui
import config
  
""" APIs for GUI integration """

def init_gui():
  gui.gtk_init_ui()
  pass


def send_text_msg(text):
  msg = "node:textmsg:" + text
  instance.gmutex.acquire()
  log_text_msg(instance.name, text)
  gui.append_chat_msg(time.strftime("%H-%M-%S"), instance.name, text)
  for peer in network.get_connection_list():
    if peer == instance.name:
      continue;
    network.send(peer, msg)
  instance.gmutex.release()


def log_text_msg(sender, text):
  instance.chat_msgs += ":" + time.strftime("%H-%M-%S") + "#" + sender + "#" + text


def received_text_msg(sender, text):
  log_text_msg(sender, text)
  gui.append_chat_msg(time.strftime("%H-%M-%S"), sender, text)
  pass


def update_map_loc(name, latitude, longitude):
  strs = instance.map_loc.split(":")
  new_map_loc = "map"
  found = False
  for i in range(1, len(strs)):
    loc = strs[i]
    data = loc.split("#")
    if data[0] == name:
      found = True
      new_map_loc += ":" + name + "#" + latitude + "#" + longitude + "#" + chr(65 + config.get_node_index(name))
    else:
      new_map_loc += ":" + loc
  if found == False:
    new_map_loc += ":" + name + "#" + latitude + "#" + longitude + "#" + chr(65 + config.get_node_index(name))
  instance.map_loc = new_map_loc


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
