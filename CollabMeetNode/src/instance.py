import threading

"""Global variables defined here"""
name = ''
local_ip = ''
listen_port = 0
is_master = False
curr_master = ''
meeting_id = 123
master_thread = None
nodes = []
heartbeat_time = dict()
has_exited = False

gmutex = threading.Lock()

"""Constants"""
HEARTBEAT_SECS = 5
HEARTBEAT_TIMEOUT = 30
CONN_RETRY_SECS = 5

SENDER = 0
MODULE = 1
MSGTYPE = 2

NODECOUNT = 3