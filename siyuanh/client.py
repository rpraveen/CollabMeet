#!/usr/bin/env python

import sys, os
import pygtk, gtk, gobject
import pygst
pygst.require("0.10")
import gst

class GTK_Main:

	def __init__(self, host_ip, port):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Video-Player")
		window.set_default_size(800, 500)
		window.connect("destroy", gtk.main_quit, "WM destroy")
		vbox = gtk.VBox()
		window.add(vbox)
		hbox = gtk.HBox()
		vbox.pack_start(hbox, False)
#		self.entry = gtk.Entry()
#		hbox.add(self.entry)
		self.button = gtk.Button("Start")
		hbox.pack_start(self.button, False)
		self.button.connect("clicked", self.start_stop)
		self.movie_window = gtk.DrawingArea()
		vbox.add(self.movie_window)
		
#		self.playButton = gtk.Button(stock='gtk-media-play')
#		self.playButton.connect("clicked", self.OnPlay)
#		self.stopButton = gtk.Button(stock='gtk-media-stop')
#		self.stopButton.connect("clicked", self.OnStop)
#		self.quitButton = gtk.Button(stock='gtk-quit')
#		self.quitButton.connect("clicked", self.OnQuit)
#		self.bb = gtk.HButtonBox()
#		self.bb.add(self.playButton)
#		self.bb.add(self.stopButton)
#		self.bb.add(self.quitButton)
#		vbox.pack_start(self.bb)
		
		window.show_all()

		self.player = gst.Pipeline("player")
		self.tcpsrc = gst.element_factory_make("tcpserversrc")
		print "host_ip = " + host_ip
		print "port = %d" % port
		self.tcpsrc.set_property("host", host_ip)
		self.tcpsrc.set_property("port", port)

		self.decodebin = gst.element_factory_make("decodebin2")
		self.queue1 = gst.element_factory_make("queue")
		self.queue2 = gst.element_factory_make("queue")
		self.autoconvert = gst.element_factory_make("autoconvert")
		self.audioconvert = gst.element_factory_make("audioconvert")
		self.audiosink = gst.element_factory_make("autoaudiosink") 
		self.videosink = gst.element_factory_make("autovideosink")
		videocap = gst.Caps("video/x-raw-yuv")
		self.filter_ = gst.element_factory_make("capsfilter")
		self.filter_.set_property("caps", videocap)
		self.colorspace = gst.element_factory_make("ffmpegcolorspace")
		
		self.player.add(#self.filesrc, 
				self.tcpsrc,
				self.decodebin, #self.autoconvert, 
				self.audioconvert, self.queue1, self.queue2, self.filter_,
				self.colorspace, self.audiosink, self.videosink)
		gst.element_link_many(#self.filesrc, 
				self.tcpsrc, self.decodebin)
		gst.element_link_many(self.queue1, #self.autoconvert, 
				self.filter_,
				self.colorspace, self.videosink)
		gst.element_link_many(self.queue2, self.audioconvert, self.audiosink)

		bus = self.player.get_bus()
		bus.add_signal_watch()
		bus.enable_sync_message_emission()
		bus.connect("message", self.on_message)
		bus.connect("sync-message::element", self.on_sync_message)
		if not self.decodebin is None:
			self.decodebin.connect("pad_added", self.decodebin_pad_added)

	def decodebin_pad_added(self, decodebin, pad):
		compatible_pad = None
		caps = pad.get_caps()
		name = caps[0].get_name()
		print "\n cap name is = ", name
		if name[:5] == 'video':
		    compatible_pad = self.queue1.get_compatible_pad(pad, caps)
		elif name[:5] == 'audio':
		    compatible_pad = self.queue2.get_compatible_pad(pad, caps)

		if compatible_pad:
			pad.link(compatible_pad)
	
	def start_stop(self, w):
		if self.button.get_label() == "Start":
			self.button.set_label("Stop")
			self.player.set_state(gst.STATE_PLAYING)
		else:
			self.player.set_state(gst.STATE_NULL)
			self.button.set_label("Start")

	def on_message(self, bus, message):
		t = message.type
		if t == gst.MESSAGE_EOS:
			self.player.set_state(gst.STATE_NULL)
			self.button.set_label("Start")
		elif t == gst.MESSAGE_ERROR:
			self.player.set_state(gst.STATE_NULL)
			err, debug = message.parse_error()
		   	print "Error: %s" % err, debug
		   	self.button.set_label("Start")

	def on_sync_message(self, bus, message):
		if message.structure is None:
			return
		message_name = message.structure.get_name()
		if message_name == "prepare-xwindow-id":
			imagesink = message.src
			imagesink.set_property("force-aspect-ratio", True)
			gtk.gdk.threads_enter()
			imagesink.set_xwindow_id(self.movie_window.window.xid)
		 	gtk.gdk.threads_leave()

	def OnPlay(self, widget):
		print "play"
#		self.sink.set_xwindow_id(self.da.window.xid)
		self.player.set_state(gst.STATE_PLAYING)

	def OnStop(self, widget):
		print "stop"
		self.player.set_state(gst.STATE_READY)

	def OnQuit(self, widget):
		gtk.main_quit()


if len(sys.argv) != 3:
	print "Usage: %s [host_ip] [port]" % sys.argv[0]
	sys.exit(1)
GTK_Main(sys.argv[1], int(sys.argv[2]))
gtk.gdk.threads_init()
gtk.main()
