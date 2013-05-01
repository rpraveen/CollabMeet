#!/usr/bin/pythonw

import urllib
import codecs
from pygeocoder import Geocoder
from googlemaps import GoogleMaps
from motionless import AddressMarker, LatLonMarker,DecoratedMap, CenterMap, VisibleMap
import gui
import api
import instance
import threading
import time

def generate_map_and_desc(gps_data, marker_list):
    api_key='AIzaSyBepV-5hoVd8xzwkdE93I0eRKf2jTlys3U'
    gmaps = GoogleMaps(api_key)
    gps=gps_data
    try:
        result = Geocoder.reverse_geocode(gps_data[0],gps_data[1])
        destination = str(result)
    except:
        destination = 'N/A'
    dmap=DecoratedMap(size_x=400,size_y=400)
    for i in range(0, len(marker_list)):
        dmap.add_marker(LatLonMarker(lat=marker_list[i][0], lon=marker_list[i][1], label=marker_list[i][2]))
    cmap = CenterMap(lat=gps[0],lon=gps[1], zoom=12)
    map_url=dmap.generate_url()
    f=open(instance.name + '_map.png','wr')
    f.write(urllib.urlopen(map_url).read())
    f.close()
    return destination

def gen_map():
    instance.gmutex.acquire()
    api.update_map_loc('alice', '40.442885', '-79.94263')
    api.update_map_loc('bob', '40.444885', '-79.94463')
    instance.gmutex.release()
    map_loc_str = instance.map_loc
    marker_list = []
    strs = map_loc_str.split(":")
    if len(strs) == 1:
        return
    for i in range(1, len(strs)):
        loc = strs[i]
        data = loc.split("#")
        marker_list.append([float(data[1]), float(data[2]), data[3]])
    gps_data = [marker_list[0][0], marker_list[0][1]]
    des = generate_map_and_desc(gps_data, marker_list)
    gui.update_image(instance.name + '_map.png')

class MapThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon=True
    self.start()

  def run(self):
    while not instance.has_exited:
      time.sleep(5)
      gen_map()