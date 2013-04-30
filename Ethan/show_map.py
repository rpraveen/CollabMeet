#!/usr/bin/pythonw
# coding:utf-8 

import sys
sys.path.append("/Applications/Python 3.3/PyQt-mac-gpl-4.10")
from PyQt4 import Qt
import urllib2
import os
from map_decode import *

class Map(Qt.QDialog):
    def __init__(self,parent=None):
        super(Map,self).__init__(parent)
        
        handler=urllib2.HTTPBasicAuthHandler()
        self.opener=urllib2.build_opener(handler)

        self.mapshow=Qt.QLabel()
        self.latitude_label=Qt.QLabel(u'Latitude')
        self.longitude_label=Qt.QLabel(u'Longitude')
        self.latitude_edit=Qt.QLineEdit()
        self.longitude_edit=Qt.QLineEdit()
        self.button=Qt.QPushButton(u'Locate')
        self.showtext=Qt.QLabel(u'Location')
        self.combox=Qt.QComboBox()
        self.combox.addItem(u'Normal')
        self.combox.addItem(u'Satealite')

        self.connect(self.button,Qt.SIGNAL('clicked()'),self.show_map)
        self.connect(self.combox,Qt.SIGNAL('currentIndexChanged(int)'),self.changemap)
        #self.mapshow.setScaledContents(True)

        layout=Qt.QGridLayout(self)
        layout.addWidget(self.latitude_label,0,0,1,1)
        layout.addWidget(self.latitude_edit,0,1,1,1)
        layout.addWidget(self.longitude_label,0,2,1,1)
        layout.addWidget(self.longitude_edit,0,3,1,1)
        layout.addWidget(self.button,0,4,1,1)
        layout.addWidget(self.combox,0,5,1,1)
        layout.addWidget(self.mapshow,1,0,15,6)
        layout.addWidget(self.showtext,16,0,1,6)

        self.setWindowTitle(u'CollabMeet')

    def show_map(self):
        latitude=float(self.latitude_edit.text())
        longitude=float(self.longitude_edit.text())
        if latitude is None:
            self.showtext.setText(u'latitude is null!')
            return
        if longitude is None:
            self.showtext.setText(u'longitude is null!')
            return
        try:
            latitude=float(latitude)
            longitude=float(longitude)
        except:
            self.showtext(u'input format is not right!')
            raise

        gps_data=[latitude,longitude]
        
        mode = self.combox.currentIndex()
        marker_list = [[(gps_data[0]+0.001), (gps_data[1]+0.001)],[40.4433, -79.9436]]
        des = generate_map_and_desc(gps_data,mode,marker_list)
                #print(map_url)
                #map_file=self.opener.open(map_url)
                #f=open('tmp.png','wr')
                #f.write(map_file.read())
                #f.close()
        self.showtext.setText(des)
        self.mapshow.clear()
        picture=Qt.QImage('./tmp.png')
        self.mapshow.setPixmap(Qt.QPixmap.fromImage(picture))
        #self.mapshow.append('<img src="./tmp.png">')

    def changemap(self,tmp):
        self.show_map()


        

app=Qt.QApplication(sys.argv)
map=Map()
map.show()
tmp=app.exec_()
if os.path.isfile('tmp.png'):
    os.remove('tmp.png')
sys.exit(tmp)
