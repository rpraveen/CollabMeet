#!/usr/bin/env python

# It's a gstreamer TCP/IP client that sends a file
# through a tcpclientsink to a server on localhost

import gobject, pygst
pygst.require("0.10")
import gst, sys

if len(sys.argv) != 4:
	print "Usage: %s [server_ip] [server_port] [path_to_video]" % sys.argv[0];
	sys.exit(1)
# create a pipeline and add [ filesrc ! tcpclientsink ]
pipeline = gst.Pipeline("client")

src = gst.element_factory_make("filesrc", "source")
src.set_property("location", sys.argv[3])
pipeline.add(src)

client = gst.element_factory_make("tcpclientsink", "client")
pipeline.add(client)
client.set_property("host", sys.argv[1])
client.set_property("port", int(sys.argv[2]))
src.link(client)

pipeline.set_state(gst.STATE_PLAYING)

# enter into a mainloop
loop = gobject.MainLoop()
loop.run()
