import network
import instance
import master
import time
import gui
import config
import video
  
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

def update_video_source(name, ip, port):
  changed = False
  if instance.curr_video_name != name:
    changed = True
  instance.curr_video_name = name
  instance.curr_video_ip = ip
  instance.curr_video_port = port
  if changed:
    video.stop_client()
    video.create_client()
