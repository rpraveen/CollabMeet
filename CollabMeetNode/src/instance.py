"""Global variables defined here"""
name = ''
local_ip = ''
listen_port = 0
is_master = False
curr_master = ''
master_thread = None
nodes = []

"""Constants"""
HEARTBEAT_SECS = 5
HEARTBEAT_TIMEOUT = 30