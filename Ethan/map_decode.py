#!/usr/bin/pythonw

import urllib
import codecs
from pygeocoder import Geocoder
from googlemaps import GoogleMaps
from motionless import AddressMarker, LatLonMarker,DecoratedMap, CenterMap, VisibleMap

def generate_map_and_desc(gps_data,mode,marker_list):
    ischina=False
    api_key='AIzaSyBepV-5hoVd8xzwkdE93I0eRKf2jTlys3U'
    gmaps = GoogleMaps(api_key)
    gps=gps_data
    try:
        result = Geocoder.reverse_geocode(gps_data[0],gps_data[1])
        destination = str(result)
    except:
        destination = 'N/A'
    
    if mode==0:
        dmap=DecoratedMap(size_x=400,size_y=400)
    else:
        dmap=DecoratedMap(size_x=400,size_y=400, maptype='satellite')

    dmap.add_marker(LatLonMarker(lat=gps[0],lon=gps[1],label='A'))
    for i in range(0, len(marker_list)):
        dmap.add_marker(LatLonMarker(lat=marker_list[i][0],lon=marker_list[i][1],label=chr(66+i)))

    cmap = CenterMap(lat=gps[0],lon=gps[1], zoom=12)
    map_url=dmap.generate_url()
    print(map_url)
    f=open('tmp.png','wr')
    f.write(urllib.urlopen(map_url).read())
    f.close()

    return destination
