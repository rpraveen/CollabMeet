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

class markui(threading.Thread):
  def __init__(self):
    """display main window"""
    threading.Thread.__init__(self)
    self.daemon=True
    self.start()  

  def send_message(self, message=None):
    text = self.input_text.get_text()
    print "in send_message: %s" % (text)
    api.send_text_msg(text) #send over the network    

    #also show on the chat box
    buf = self.chattextview.get_buffer()
    eob = buf.get_end_iter()
    buf.insert(eob,"\n"+text)

  def print_data(msg):
    msg = msg + "\n"
    now = time.strftime("%H:%M:%S")
    msg = "["+now+"]: "+msg
    buf = self.chattextview.get_buffer()
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


  ##callback##
  def button1_clicked(self, widget):
    print "hello"
    self.main_iteration()#XXX

  def destroy(self, widget):
    print "destroy occured"
  def on_entry1_key_press_event(self, widg, event):
    if event.keyval==gtk.keysyms.Return:
        self.send_message()
        self.input_text.set_text("")
  def on_connect_button_click(self, arg):
    self.main_iteration()



  def run(self):
    gladefile="p11.glade"
    wname="markui"
    self.wTree=gtk.glade.XML(gladefile,wname)
    
    dic={"on_button1_clicked":self.button1_clicked, 
         "on_markui_destroy":(gtk.main_quit),
         "on_entry1_key_press_event":self.on_entry1_key_press_event,
         "destroy":self.destroy}

    self.wTree.signal_autoconnect(dic)
    self.window = self.wTree.get_widget("markui")
    self.input_text = self.wTree.get_widget("entry1")
    self.chattextview = self.wTree.get_widget("chattextview");
    self.window.show()
 
    #self.main_iteration()
    gtk.main()

def button1_clicked(widget):
  print "hello"
  global input_text
  text = input_text.get_text()
  api.send_text_msg(text) #send over the network    

def destroy(self, widget):
  print "destroy occured"

def on_entry1_key_press_event(widg, event):
  pass

def on_connect_button_click(self, arg):
  pass


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
  chattextview = wTree.get_widget("chattextview");
  window.show()
 
  #self.main_iteration()
  gtk.main()


#for stand alone application
if __name__ == "__main__":
  a=markui()
  gtk.main()
