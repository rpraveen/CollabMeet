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
import time

input_text = None
chattextview = None

def send_message(message = None):
  global input_text
  text = input_text.get_text()
  api.send_text_msg(text) #send over the network    

  #also show on the chat box
  global chattextview
  buf = chattextview.get_buffer()
  eob = buf.get_end_iter()
  buf.insert(eob,"\n"+text)

def print_data(msg):
  msg = msg + "\n"
  now = time.strftime("%H:%M:%S")
  msg = "["+now+"]: "+msg
  global chattextview
  buf = chattextview.get_buffer()
  buf.insert(buf.get_end_iter(), msg)


def main_iteration(self):
  while 1:
    #try:
    m = api.recv()
    #except:
    #  print "exception in api.recv"

    if m != None:
      print_data("["+m+"]")
    else:
      print "no message so far"

    print "in main_iteration.."
    time.sleep(1) #check 0.01

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
  #main_iteration()
  gtk.main()
