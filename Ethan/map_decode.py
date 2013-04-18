#!/usr/bin/pythonw

import codecs
from googlemaps import GoogleMaps
from motionless import AddressMarker, LatLonMarker,DecoratedMap, CenterMap, VisibleMap

def generate_map_and_desc(gps_data,mode):
    ischina=False
    api_key='AIzaSyBepV-5hoVd8xzwkdE93I0eRKf2jTlys3U'
    gmaps = GoogleMaps(api_key)
    gps=gps_data
    #destination = gmaps.latlng_to_address(gps[0],gps[1])
    destination='N/A'
    if mode==0:
        dmap = DecoratedMap(size_x=600,size_y=400)
        dmap.add_marker(LatLonMarker(lat=gps[0],lon=gps[1],label='A'))
    else:
        dmap=DecoratedMap(size_x=600,size_y=400,maptype='satellite')
        dmap.add_marker(LatLonMarker(lat=gps_data[0],lon=gps_data[1],label='A'))
    cmap = CenterMap(lat=gps[0],lon=gps[1], zoom=12)
    map_url=dmap.generate_url()
    return (map_url,destination)
