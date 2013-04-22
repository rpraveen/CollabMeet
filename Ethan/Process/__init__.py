mport os, socket, threading,\
       logging, sys, signal
import subprocess, time
import shutil,random,math
import Pyro.core, Pyro.naming
from remoteClass import remoteClass
from ControlClass import ControlClass
from hashlib import sha1
from ChordProcessRecord import ChordProcessRecord
from fileObject import fileObject
import thread
#Enable debugging/ send to stderr
#logging.basicConfig(level=logging.DEBUG)

class ChordProcess(threading.Thread):
    
    SUCCESSOR_LIST_SIZE = 6 
    KEY_LENGTH = 32
    LOOKUP_RETRIES = 5
    PERIOD = 3
    CHURN_RATE = 0
    MIN_EXP_TIME = 8
    
    def __init__(self,portNumber,bootstrapNodePort,churn,controlPortNumber):
        "Chord Process constructor"
        threading.Thread.__init__(self)
        
        
        # CHORD Client constructs
        self._successor     = ChordProcessRecord()
        self._predecessor   = ChordProcessRecord()
        self._successorList = range(1,self.SUCCESSOR_LIST_SIZE)
        
        # "Initialize" the finger Table
        self._fingerTable = range(0,self.KEY_LENGTH)
        
        # Use the process id as unique id
        self._processID  = os.getpid()
        self._localClient = ChordProcessRecord(self.assignHashKey(portNumber),int(portNumber))
        self._bootstrapNodePort = int(bootstrapNodePort)
        self._remoteClassInstance = remoteClass(self)
        self._controlClassInstance = ControlClass(self)
        self.CHURN_RATE = churn
        # Initialize the next pointer for use in fingerTable
        self._next = 0
        self._fingerTableFull =False
        # Process is "ON"
        self._status = True
        
        # Create directory for file storing
        self._dir = self.createDir()
        # Start local server
        thread.start_new_thread(self.localServer,())
        
        # Find the server of the Chord Control process
        self._controlProcess = Pyro.core.getProxyForURI("PYRONAME://{0}".format(controlPortNumber)) 
        
        print "Node {0} activated on port {1}.".format(self._localClient.getKey(),self._localClient.getPortNumber())    
    
    def assignHashKey(self,objectID):
        "Given an objectID,returns a unique\
        160-bit key, using SHA1." 
        #Call the SHA-1 function to get a key
        
        key = sha1(repr(objectID)).hexdigest()
        return key[(160-self.KEY_LENGTH)/4:]

    def createDir(self):
        "Make a new folder on the disk for storing files. If there already is one do nothing"
        if not os.path.isdir(self._localClient.getKey()):
            #logging.debug("Creating folder {0}....".format(self._localClient.getKey()))
            os.mkdir(self._localClient.getKey())
        return self._localClient.getKey()
    
    def getfileExists(self,fileName):
        "Given a fileName it returns True if the file exists \
        on the disc or False otherwise"
        if os.path.isfile(self._dir + '/' + fileName):
            return True
        else:
            return False
    
    def localServer(self):
        "A second thread of execution, upon which\
        a server is running, in order to read any\
        incoming requests"
        
        Pyro.core.initServer()
        ns=Pyro.naming.NameServerLocator().getNS()
        self._daemon=Pyro.core.Daemon()
        self._daemon.useNameServer(ns)
        
        uri=self._daemon.connect(self._remoteClassInstance,str(self._localClient.getPortNumber()))
        
        logging.debug("{0}: Listening for incoming messages on {1}:{2}".format(self._localClient.getKey(),uri,self._daemon.port))
        
        self._daemon.setTimeout(3) 
        self._daemon.requestLoop()
        
        thread.exit()
        
    def controlServer(self):
        
        Pyro.core.initServer()
        ns=Pyro.naming.NameServerLocator().getNS()
        self._cdaemon=Pyro.core.Daemon()
        self._cdaemon.useNameServer(ns)
        
        uri=self._cdaemon.connect(self._controlClassInstance,str(self._localClient.getPortNumber()+1))
        
        logging.debug("{0}: Listening for Control messages on {1}:{2}".format(self._localClient.getKey(),uri,self._cdaemon.port))
        
        self._cdaemon.requestLoop() 
    
    def localFileInsert(self,fileName):
        "Copies the given file to the self._dir directory"
        try:
            shutil.move(fileName,self._dir + '/' + fileName)
            #logging.debug("File copied locally succesfully")
            return True
        except:
            #logging.error("Local File copy failed")
            return False
            
    
    def fileInsert(self,fileName):
        "Given the name of a file, this method inserts the\
         file into the CHORD DHT"
         
        file = fileObject(fileName,self.assignHashKey(fileName)) 
        fileSuccessor = self.lookup(file.getKey())
        print "Key of file {0} is {1}".format(fileName,file.getKey())
        if fileSuccessor.getKey() == self._localClient.getKey():
            self.localFileInsert(fileName)
            logging.debug("File {0} successfully inserted locally".format(file.getName()))
        else:
            logging.debug("Inserting file: {0} to node {1}".format(file.getName(),fileSuccessor.getKey()))
            if fileSuccessor.passFile(file):
                #logging.debug("File copied successfully")
                return True
            else:
                #logging.error("File copy failed")
                return False
              
    def getPassedFile(self,file):
        "Stores the file on the local directory"
        try:
            self.makeFileObjectIntoFile(file)
            return True
        except:
            return False
    
    def makeFileObjectIntoFile(self,file):
        "Creates a file from a list which contains lines of files"
        f = open(self._dir + '/' + file.getName(),'a')
        for line in file.getData():
            f.write(line)
        f.close()
            
        
    def fileSearch(self,fileName):
        "Given a file name, this process makes a\
        lookup for the file over the CHORD DHT"

        fileKey = self.assignHashKey(fileName)
        (fileSuccessor,steps) = self.lookup(fileKey,0)
        if fileSuccessor.fileExists(fileName):
            logging.debug("{0}: File {1} exists in {2}".format(self._localClient.getKey(),fileName,fileSuccessor.getKey()))
            return fileSuccessor.getKey(),steps
        else:
            logging.warning("{0}: File {1} could not be found".format(self._localClient.getKey(),fileName))
            return None,steps
        
        
    def lookup(self,lookupKey,steps = None):
        "Given a lookup key, this method returns the\
        IP address(port Number) of the process that is the\
         successor(lookupKey)"
        
        #logging.debug("Lookup:{0}: Looking up key {1}".format(self._localClient.getKey(),lookupKey))
        if self.isInRange(self._localClient.getKey(),self._successor.getKey(),lookupKey,">="):
            if steps != None:
                return (self._successor,steps+1)
            else:
                return self._successor
        else :
            #logging.debug("Lookup: looking into the finger table for key:{0}".format(lookupKey))
            if steps!=None:
                precedingNode,retSteps = self.findSuccessor(self.closestPrecedingNode(lookupKey),lookupKey,steps)
            else:
                precedingNode = self.findSuccessor(self.closestPrecedingNode(lookupKey),lookupKey)
            if not precedingNode.isSet():
                logging.debug("{0} Lookup: Preceding node is not set.".format(self._localClient.getKey()))
            if steps != None:
                return (precedingNode,retSteps+1)
            else:
                return precedingNode
    
    def findSuccessor(self,node,lookupKey,steps = None):
        i=0
        success = False
        while success == False and i < self.LOOKUP_RETRIES :
            i = i+1
            try:
                node = node.findSuccessor(lookupKey,steps)
                success = True
            except:
                # find the next best preceding node of the lookupKey
                node = self.closestPrecedingNode(node.getKey())
                logging.debug("{0} Find successor failed.Trying node {1}".format(self._localClient.getKey(),node.getKey()))
        
        return node
            

    def isInRange(self,startKey,endKey,searchKey,comparator = ">"):
        "Returns True if the searchKey is between the\
        startKey and the endKey in the CHORD ring"
        if comparator == ">":
            comparison= startKey > endKey
        else :
            comparison= startKey >= endKey
        
        if comparison:
            if searchKey > startKey or searchKey < endKey:
                return True
        elif searchKey > startKey and searchKey < endKey:
            return True
        return False
            
    def closestPrecedingNode(self,lookupKey):
        "Given a lookupKey, the successor list and finger table\
        is accessed in order to find the node that is preceding the\
        lookup key, and is the closest to it."
        closestNode = ChordProcessRecord()
        #First find the closest preceding node in the successor list
        for pos in range(len(self._successorList)-1,-1,-1): 
            node = self._successorList[pos]
            if self.isInRange(self._localClient.getKey(), lookupKey, node.getKey()): 
                closestNode = node;
                break
            
        if self._fingerTableFull:
            length = self.KEY_LENGTH-1
        else :
            length = self._next-1
            
        
        #Then find the closest preceding node in the finger table
        for pos in range(length,-1,-1):
            currentKey = self._fingerTable[pos].getKey() 
            if self.isInRange(self._localClient.getKey(),lookupKey,currentKey):
                if closestNode.isSet():
                    # If the closest node found in the successor list is closer to the key...
                    if not self.isInRange(self._localClient.getKey(),currentKey,closestNode.getKey()):
                        # ...then return the closest node in the successor list
                        return closestNode
                else:
                        #... else return the finger table entry
                        return self._fingerTable[pos]
                    
        if closestNode.isSet():
            return closestNode
                
        return self._localClient
        
    def getProxy(self,portNumber):
        "Given the port in the name service,\
        returns a proxy of the remote object"
        return  Pyro.core.getProxyForURI("PYRONAME://{0}".format(portNumber))
        
    def nodeJoin(self):
        "Given a node to contact (class var), this method\
        puts the current Client in the Chord DHT. Returns TRUE\
        if the operation is successful, otherwise FALSE.\
        If contactNode is NONE, then a new ring is created."
        logging.debug("{0}:Attempting to join the CHORD network".format(self._localClient.getKey()))
        if self._bootstrapNodePort == self._localClient.getPortNumber():
            logging.debug("{0}:Creating a new Ring".format(self._localClient.getKey()))
            return self.createRing()
        else:
            self._predecessor = ChordProcessRecord()
            proxy = self.getProxy(self._bootstrapNodePort)
            self._successor   = proxy.findSuccessor(self._localClient.getKey())
            self._successorList = [self._successor for item in  range(0,self.SUCCESSOR_LIST_SIZE)]
            logging.debug("{0}:Successor found:{1}".format(self._localClient.getKey(),self._successor.getKey()))
            if self._successor.getKey() != self._localClient.getKey():
                fileObjectList = self._successor.getFiles()
                self.writeFileObjectsToDisk(fileObjectList)
            return True    
    
    def  writeFileObjectsToDisk(self,fileObjectList):
        "Given a list of fileObjects, this function creates files\
        for each one of them"
        #logging.debug("Retrieved {0} files from successor".format(len(fileObjectList)))
        for item in fileObjectList:
            self.makeFileObjectIntoFile(item)
            
    def getFiles(self):
        "Called upon join of a predecessor.Returns a\
        fileObject list of the files that should be moved\
        to the predecessor. Additionally, it removes the files from\
        the local Process."
        fileObjectList= []
        for subdir, dirs, files in os.walk(self._dir):
            for file in files:
                fileKey = self.assignHashKey(file)
                if self.isInRange(self._localClient.getKey(), self._predecessor.getKey(), fileKey):
                    fileObjectList.append(fileObject(file,fileKey))
                    os.remove(self._dir + "/" + file)
        #logging.debug("Returning file list of size {0} to predecessor".format(len(fileObjectList)))
        return fileObjectList
    
    def sendAllFiles(self):
        fileObjectList = []
        for subdir, dirs, files in os.walk(self._dir):
            for file in files:
                fileKey = self.assignHashKey(file)
                fileObjectList.append(fileObject(file,fileKey))
                os.remove(self._dir + "/" + file)
        self._successor.getAllFiles(fileObjectList)
        
         
    def getAllFiles(self,fileObjectList):
        self.writeFileObjectsToDisk(fileObjectList)
        return True
    
    def nodeLeave(self,leaveMode = "voluntary"):
        "With this method, the current Client announces\
        its departure from the Chord ring, and all its files\
        are migrated to its successor.Returns TRUE on success"
        if leaveMode == "voluntary":
            if self._successor.getKey() != self._localClient.getKey():
                self.sendAllFiles()
        #logging.debug("Shutting down daemon")
        self._daemon.shutdown()
        #logging.debug("All Files sent to successor: {0} Got to go now....Bye Bye!".format(self._successor.getKey()))
        return True
    
    def createRing(self):
        "This CHORD client instance is the first in the network"
        self.predecessor = ChordProcessRecord()
        # The client is its own successor        
        self._successor   = ChordProcessRecord(self._localClient.getKey(),self._localClient.getPortNumber())
        self._successorList = [self._successor for item in  range(0,self.SUCCESSOR_LIST_SIZE)]
        return True

    def stabilize(self):
        "This method runs periodically on the client,\
        in order to learn about newly joined nodes."
        logging.debug("{0}:Stabilize ".format(self._localClient.getKey()))
        
        try:
            successorsPredecessor = self._successor.predecessor()
            if successorsPredecessor.isSet():
                logging.debug("{0} Stabilize:Got successor's predecessor: {1}".format(self._localClient.getKey(),successorsPredecessor.getKey()))
                if self.isInRange(self._localClient.getKey(),self._successor.getKey(),successorsPredecessor.getKey(),">="):
                    logging.debug("{0}: Stabilize: Changing successor to {1}".format(self._localClient.getKey(),successorsPredecessor.getKey()))
                    self._successor = successorsPredecessor  
                    self._fingerTable[0] = self._successor
                
            self.fixSuccessorList()
            self._successor.notify(self._localClient)
            
            if self._successor.getKey() != self._localClient.getKey():
                fileObjectList = self._successor.getFiles()
                if fileObjectList != None:
                    self.writeFileObjectsToDisk(fileObjectList)
                
        except Pyro.errors.ProtocolError:
            logging.warning("{0}: Stabilize: Communication failed when trying to contact node {1}".format(self._localClient.getKey(),self._successor.getKey()))
            self.setNewSuccessor()
            
            
            
    def setNewSuccessor(self):
        "After successor failure, a new successor must be\
        chosen from the successor list.Consequently the successor\
        list of the new successor must be chosen"
        i=0
        while i < len(self._successorList)\
            and isinstance(self._successorList[i],ChordProcessRecord)\
            and not self._successorList[i].isAlive():
            i = i + 1
            
        if i==len(self._successorList):
            return
            
        logging.debug("{0} setNewSuccessor: Due to successor failure, setting new successor to {1}".format(self._localClient.getKey(),self._successorList[i].getKey()))
        self._successor = self._successorList[i]
        self.fixSuccessorList()

            
    def fixSuccessorList(self):
        "Retrieve the successor list of the successor and\
        append it to the local successorList"

        successorsSucList = self._successor.getSuccessorList()  
        if successorsSucList != None:      
            sucLength = len(successorsSucList)
            self._successorList = [self._successor]
            self._successorList[1:sucLength] =  successorsSucList[0:sucLength-1] 
            #logging.debug("FixSuccessorList:Got successor list from successor")
    
    def getSuccessorList(self):
        "Getter for Successor list"
        return self._successorList

    
    def getNotified(self,predecessor):
        "This method updates the successor's knowledge about\
        who is his predecessor."
        
        #logging.debug("getNotified:{0}: Predecessor notification by {1} ".format(self._localClient.getKey(),predecessor.getKey()))
        if not self._predecessor.isSet():
            #logging.debug("getNotified:{0}: Notification:Changing predecessor to {1} ".format(self._localClient.getKey(),predecessor.getKey()))
            self._predecessor = predecessor
        if self.isInRange(self._predecessor.getKey(), self._localClient.getKey(), predecessor.getKey(),">="):
            #logging.debug("getNotified:{0}: Notification:IS IN RANGEChanging predecessor to {1} ".format(self._localClient.getKey(),predecessor.getKey()))
            self._predecessor = predecessor
        
    def reportStatus(self):
        print("*********************************************************")
        print("*                  STATUS:                              *")
        print("* ------------------------------------------------------*")
        print("* Process Key= {0}                                  *".format(self._localClient.getKey()))
        print("* Successor  = {0}                                  *".format(self._successor.getKey()))
        print("* Predecessor= {0}                                     *".format(self._predecessor.getKey()))
        if self._fingerTableFull:
            entries = self.KEY_LENGTH
        else:
            entries = self._next  
        print("* Finger table entries: {0}                               *".format(entries))
        print("*********************************************************")
    
        
    def fixFingers(self):
        "New nodes initialize their finger tables with\
        fixFingers and existing nodes incorporate new\
        nodes into their finger tables"
        try:
            if self._next >= self.KEY_LENGTH:
                self._next = 0
                self._fingerTableFull = True
            lookupKey = hex(int(self._localClient.getKey(),16) + 2**self._next)[2:]
            #logging.debug("fixFingers: Lookup key is {0}".format(lookupKey))
            self._fingerTable[self._next] = self.lookup(lookupKey)
            self._next = self._next + 1
            if(self._next == 32):
                print "{0} :Finger table full".format(self._localClient.getKey())
            #logging.debug("fixFingers:Fixing finger position: {0} with key: {1}".format(self._next -1,self._fingerTable[self._next-1].getKey()))
        except Pyro.errors.ProtocolError:
            logging.warning("FixFingers: Communication failed")
        
    
    def callPeriodicFunctions(self):
        self.checkPredecessor()
        self.stabilize()    
        self.fixFingers()
        if not self._predecessor.isSet():
            self.reportStatus()
        
    def killChordProcess(self,signo,frame):
        print "Caught signal!"
        self._daemon.shutdown()
        exit()
      
    def checkPredecessor(self):
        "Check whether the predecessor node\
        is alive and well.If not, set the predecessor\
        to a null Node"
        if self._predecessor.isSet() and not self._predecessor.isAlive():
            logging.debug("{0} Predecessor is not responding.Setting predecessor to None".format(self._localClient.getKey()))
            self._predecessor = ChordProcessRecord()
              
            
    def getPredecessor(self):
        return self._predecessor
    
    def setBootstrapNode(self,port):
        self._bootstrapNodePort = port
        
    def setStatus(self,status):
        self._status = status
        
    def getStatus(self):
        return self._status
        
    def setPeriod(self,period):
        self.PERIOD = period
        
    def failure(self,signum, frame):
        "Fail or respawn according to the churn rate"
        if(random.random() < self.CHURN_RATE):
            if self._status:
                if not self._controlProcess.notifyControl(self._localClient.getPortNumber(),False):
                    return
                print("{0} :Switching OFF daemon".format(self._localClient.getKey()))
                self._status = False
                self._daemon.shutdown()
            else:
                print("{0} :Switching ON daemon".format(self._localClient.getKey()))
                self._bootstrapNodePort =self._controlProcess.requestBootstrapNode()
                if self._bootstrapNodePort!=None:
                    thread.start_new_thread(self.localServer,())
                    self._status = True
                    
                self._controlProcess.notifyControl(self._localClient.getPortNumber(),True)
                     
        interval = int(math.ceil(random.expovariate(1)*6*self.PERIOD/self.CHURN_RATE))
#        print "Interval is ",interval
        if(interval < self.MIN_EXP_TIME):
            interval = self.MIN_EXP_TIME
        signal.alarm(interval)
        
def main():
    "Main function. Creates a server thread \
    and and puts the client in the Chord ring"
    
    if len(sys.argv) !=4:
        print "Usage: Process PortNumber BoostrapNode_Port Churn_Rate"
        exit()
    
    # Create a new local instance ,4900 is the "port" of the master process   
    localClient = ChordProcess(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),4900)


    #Start listening for control messages
    thread.start_new_thread(localClient.controlServer,())
        
    time.sleep(1)
    
    #Join the Chord ring via the bootstrap node
    localClient.nodeJoin()
    
    signal.signal(signal.SIGALRM, localClient.failure)
    if(localClient.CHURN_RATE!=0):
        signal.alarm(10)
    
    # Call periodic functions every PERIOD seconds        
    while(True):
        time.sleep(localClient.PERIOD)
        if localClient._status:
            localClient.callPeriodicFunctions()

if __name__ == "__main__":
    main()


    


    
        
