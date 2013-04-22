import Pyro.core
class ControlClass(Pyro.core.ObjBase):
    def __init__(self,processHandle):
            Pyro.core.ObjBase.__init__(self)
            self._processHandle = processHandle 
    def searchFile(self,fileName):
        return self._processHandle.fileSearch(fileName)
    def insertFile(self,fileName):
        try:
            fileName = fileName.partition('/')[2]
            return self._processHandle.fileInsert(fileName)
        except:
            return None
    def getKey(self):
        return self._processHandle._localClient.getKey()
    def getPort(self):
        return self._processHandle._localClient.getPortNumber()
    def setPeriod(self,period):
        return self._processHandle.setPeriod(period)
    def isAlive(self):
        "Check whether the current node is available"
        try:
            if self._processHandle.getStatus():
                return True
            else:
                return False
        except:
            return False
    def requestBootstrapNode(self):
        try:
            return self._processHandle.getBootstrapNode()
        except:
            return None
    def notifyControl(self,port,status):
        return self._processHandle.notifyControl(port,status)
            
        
