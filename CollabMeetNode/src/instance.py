import threading

"""Global variables defined here"""
name = ''
local_ip = ''
listen_port = 0
meeting_id = 123
video_port = 12344

is_master = False
curr_master = ''
master_thread = None
nodes = []
heartbeat_time = dict()
has_exited = False
last_heartbeat_rcvd = 0

curr_video_name = 'none'
curr_video_ip = '0.0.0.0'
curr_video_port = 0
initialized = False
gui_inited = False

child_pid = 0

chat_msgs = "chat"

map_loc = "map"

gmutex = threading.Lock()

"""Constants"""
HEARTBEAT_SECS = 5
HEARTBEAT_TIMEOUT = 15
CONN_RETRY_SECS = 5

SENDER = 0
MODULE = 1
MSGTYPE = 2

NODECOUNT = 3
