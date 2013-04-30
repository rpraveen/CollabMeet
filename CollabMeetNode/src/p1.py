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
import instance

input_text = None
chattextview = None

def print_data(msgtime, sender, msg):
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


def markui1():
  gladefile="p11.glade"
  wname="markui"
  wTree=gtk.glade.XML(gladefile,wname)
  dic={"on_button1_clicked":button1_clicked, 
       "on_markui_destroy":(gtk.main_quit),
       "on_entry1_key_press_event":on_entry1_key_press_event,
       "destroy":destroy}
  wTree.signal_autoconnect(dic)
  window = wTree.get_widget("markui")
  global input_text
  input_text = wTree.get_widget("entry1")
  global chattextview
  chattextview = wTree.get_widget("chattextview");
  window.show()
  gtk.main()
