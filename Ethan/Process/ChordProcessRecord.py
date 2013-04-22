import logging
import Pyro.core, Pyro.naming,\
       Pyro.errors
from remoteClass import remoteClass

class ChordProcessRecord:
    "This class holds the information that\
    is kept for a CHORD client, regarding another\
    CHORD client"
    
    TIMEOUT = 3
    
    def __init__(self,key = None,portNumber = None):
        "Create a new record"
        self._key = key
        self._portNumber = portNumber
     
    def isSet(self):
        if self._key == None or self._portNumber == None:
            return False
        return True
        
    def getPortNumber(self):
        return self._portNumber
    
    def getKey(self):
        return self._key
    
    def setPortNumber(self,newPortNumber):
        self._portNumber=newPortNumber
        
    def setKey(self,newKey):
        self._key = newKey
        
    def getProxy(self,portNumber):
        "Given the port in the name service,\
        returns a proxy of the remote object"
        proxy = Pyro.core.getProxyForURI("PYRONAME://{0}".format(portNumber))
        proxy._setTimeout(self.TIMEOUT)
        return proxy         
    
    def findSuccessor(self,lookupKey,steps = None):
        return  self.getProxy(self._portNumber).findSuccessor(lookupKey,steps)
    
    def predecessor(self):
        try:
            return self.getProxy(self._portNumber).getPredecessor()
        except:
            return ChordProcessRecord()
    
    def notify(self,predecessorProcess):
        return self.getProxy(self._portNumber).getNotified(predecessorProcess)
    
    def isAlive(self):
        try:
            return self.getProxy(self._portNumber).isAlive()
        except:
            return False
        
    def passFile(self,fileObject):
        "Given a file it calls the function that stores the file to\
        the appropriate remote object and returns success or failure correspondingly"
        #logging.debug("Sent file: {0}".format(fileObject.getName()))
        try:
            return self.getProxy(self._portNumber).getPassedFile(fileObject)
        except:
            return False
    
    def fileExists(self,fileName):
        "Respond if the file exists, or false if the node is unreachable"
        try:
            return self.getProxy(self._portNumber).fileExists(fileName)
        except:
            return False
    
    def getSuccessorList(self):
        try:
            return self.getProxy(self._portNumber).getSuccessorList()
        except:
            return None
    
    def getFiles(self):
        try:
            return self.getProxy(self._portNumber).getFiles()
        except:
            return None
    
    def getAllFiles(self,fileObjectList):
        return self.getProxy(self._portNumber).getAllFiles(fileObjectList)
    