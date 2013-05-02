#!/usr/bin/env python
try:
  import pygtk
  pygtk.required("2.0");
except:
  pass

try:
  import gtk
  import gtk.glade
except:
  print "need pyGTK  and glade"
  sys.exit(1)

import api
import threading
import network
import instance
import config

input_text = None
chattextview = None
wTree = None

def append_chat_msg(msgtime, sender, msg):
  if instance.gui_inited == False:
    return
  msg = msg + "\n"
  msgtime = msgtime.replace('-', ':', 10)
  msg = "[" + msgtime + "] " + sender + ": " + msg
  global chattextview
  buf = chattextview.get_buffer()
  buf.insert(buf.get_end_iter(), msg)

def send_message(message = None):
  global input_text
  text = input_text.get_text()
  api.send_text_msg(text) #send over the network

def on_entry1_key_press_event(widg, event):
  if event.keyval == gtk.keysyms.Return:
    send_message()
    global input_text
    input_text.set_text("")
  
def button1_clicked(widget):
  send_message(None)

def destroy(self, widget):
  print "destroy occured"

def update_image(file):
  if instance.gui_inited == False:
    return
  global wTree
  pixbuf = gtk.gdk.pixbuf_new_from_file(file)
  width = 300
  height = 300
  pixbuf = pixbuf.scale_simple(width, height, gtk.gdk.INTERP_BILINEAR)
  image = wTree.get_object("image1")
  image.set_from_pixbuf(pixbuf)

def update_meeting_info():
  if instance.gui_inited == False:
    return
  global wTree
  meetinginfo = wTree.get_object("meetinginfo");
  buf = meetinginfo.get_buffer()
  msg = ""
  msg += "< Name: " + instance.name + " >\n"
  msg += "< Meeting ID: " + str(instance.meeting_id) + " >\n"
  msg += "\nOnline Members:\n" + instance.name + "\n"
  for peer in network.get_connection_list():
    msg += peer + "\n"
  msg += "\nAll Members:\n"
  for node in instance.nodes:
    msg += chr(65 + config.get_node_index(node.name)) + ") " + node.name + "\n" 
  buf.set_text(msg)


def change_master_label():
  if instance.gui_inited == False:
    return
  global wTree
  color = gtk.gdk.color_parse("green")  #'#234fdb')
  l2 = wTree.get_object("eventbox1")
  l2.modify_bg(gtk.STATE_NORMAL, color)

	
def remove_master_label():
  if instance.gui_inited == False:
    return
  global wTree
  color = gtk.gdk.Color(30000, 30000, 30000, 255)  #'#234fdb')
  l2 = wTree.get_object("eventbox1")
  l2.modify_bg(gtk.STATE_NORMAL, color)


def gtk_init_ui():
  gladefile="p12.glade"
#  wname="markui"
  global wTree
#  wTree=gtk.glade.XML(gladefile,wname)
  wTree = gtk.Builder()
  wTree.add_from_file(gladefile)
  dic={"on_button1_clicked": button1_clicked, 
       "on_markui_destroy": gtk.main_quit,
       "on_entry1_key_press_event": on_entry1_key_press_event,
       "destroy":destroy, }
#  wTree.signal_autoconnect(dic)
  wTree.connect_signals(dic)
  window = wTree.get_object("markui")
  global input_text
  input_text = wTree.get_object("entry1")
  global chattextview
  chattextview = wTree.get_object("chattextview")

  

  #calendar = gtk.Calendar()

  instance.gmutex.acquire()
  instance.gui_inited = True
  update_meeting_info()
  instance.gmutex.release()

  if instance.is_master:
    change_master_label()
  else:
    remove_master_label()

  update_image("google_maps.jpg")

  strs = instance.chat_msgs.split(":")
  for i in range(1, len(strs)):
    chat = strs[i].split("#")
    append_chat_msg(chat[0], chat[1], chat[2])

  window.show()
  gtk.main()
