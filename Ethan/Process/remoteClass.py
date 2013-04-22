import Pyro.core,logging

class remoteClass(Pyro.core.ObjBase):
    def __init__(self,processHandle):
        Pyro.core.ObjBase.__init__(self)
        self._processHandle = processHandle
    def testRMI(self, name):
        return "{0}: Successful RMI session".format(name)
    def findSuccessor(self,lookupKey = None, steps = None):
        "This is the method that the remote process\
        can have access to, through which it can gain\
        access to the lookup operation of the local process"
        if lookupKey == None:
            return self._processHandle.lookup(self._processHandle._localClient.getKey())
        else:
            if steps!= None:
                return self._processHandle.lookup(lookupKey,steps)
            else:
                return self._processHandle.lookup(lookupKey)
    
    def getPredecessor(self):
        "Returns the predecessor ChordProcessRecord of the process\
        who receives the request"
        return self._processHandle.getPredecessor()
    def getNotified(self,predecessor):
        "Receive a possible predecessor"
        self._processHandle.getNotified(predecessor)
    
    def getPassedFile(self,fileName):
        logging.debug("in the remote object and about to receive file")
        logging.debug("Got file: {0}".format(fileName))
        return self._processHandle.getPassedFile(fileName)
    
    def isAlive(self):
        "Check whether the current node is available"
        #Do i need to contact the Process class?
        return True
    
    def fileExists(self,fileName):
        return self._processHandle.getfileExists(fileName)
    
    def getSuccessorList(self):
        return self._processHandle.getSuccessorList()
    
    def getFiles(self):
        return self._processHandle.getFiles()
    
    def getAllFiles(self,fileObjectList):
        return self._processHandle.getAllFiles(fileObjectList)
