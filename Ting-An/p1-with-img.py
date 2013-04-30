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
import time

class markui():
  def __init__(self):
    """display main window"""

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

    pixbuf = gtk.gdk.pixbuf_new_from_file("amanda-seyfried-us-open-ice-cream-cone-02.jpg")
    width = 300
    height = 300
    pixbuf = pixbuf.scale_simple(width, height, gtk.gdk.INTERP_BILINEAR)
    self.image = self.wTree.get_widget("image1")
    self.image.set_from_pixbuf(pixbuf)

    self.window.show()

    return


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


  ##callback##
  def button1_clicked(self, widget):
    print "hello"
  def destroy(self, widget):
    print "destroy occured"
  def on_entry1_key_press_event(self, widg, event):
    if event.keyval==gtk.keysyms.Return:
        self.send_message()
        self.input_text.set_text("")

if __name__ == "__main__":
  a=markui()
  gtk.main()
