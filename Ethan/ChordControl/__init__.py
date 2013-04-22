import logging, sys, os,\
       subprocess , random,\
       time, thread, math

import Pyro.core, Pyro.naming
from ControlClass import  ControlClass


#Enable debugging/ send to stderr
logging.basicConfig(level=logging.INFO)

nodeHandles = []
nodeStatus  = []

class ChordControl:
    
    def __init__(self,clients,churn):
        self._portNumber = 4900
        self._basePort = 5000
        self._bootstrapPort = 5000
        self._n_clients = clients
        self._churn_rate = churn
        self._controlClassInstance = ControlClass(self)
        self._liveNodes = 0
        #Start control server that will hand-out bootstrap nodes
        thread.start_new_thread(self.controlServer,())
    
        #Create client nodes    
        self.createClients()
    
    def createClientProcess(self,portNumber,bootstrapPort):
        "Spawn a new CHORD client process,\
        supplying it with a portto bind to"
        time.sleep(0.2)
        logging.debug("Master Process:Creating new Chord client")
        subprocess.Popen(["python","../Process/__init__.py",str(portNumber),str(bootstrapPort),str(self._churn_rate)])
        
    def getNodeHandles(self):
        "Create CHORD clients with unique portNumber\
        and a bootstrap node"    
        portNumber = self._basePort+1
        for client in range(self._n_clients):
            nodeHandles.append(self.getProxy(portNumber)) 
            nodeStatus.append(True)
            self._liveNodes+=1
            portNumber = portNumber + 2
        return nodeHandles
    
    def createClients(self):
        "Create CHORD clients with unique portNumber\
        and a bootstrap node"    
        portNumber = self._basePort
        for client in range(self._n_clients):
            self.createClientProcess(portNumber,self._bootstrapPort)
            portNumber = portNumber + 2    
            if portNumber >=5004:
                self._bootstrapPort = self._bootstrapPort + 2
    
        
        time.sleep(4)
    
        self.getNodeHandles()
        
    def isAlive(self,node):
        try: 
            return node.isAlive()
        except:
            return False
        
    
    def getProxy(self,portNumber):
        "Given the port in the name service,\
        returns a proxy of the remote object"
        proxy = Pyro.core.getProxyForURI("PYRONAME://{0}".format(portNumber))
        return proxy   
              
    def searchFile(self,pos,file):      
        node,steps = nodeHandles[pos].searchFile(file)
        print "Master Process:File {0} found in node {1} in {2} steps".format(file,node,steps)
        
        
    def controlServer(self):
        "The only purpose of this server is to\
        hand-out bootstrap ports, to nodes that\
        want to rejoin the chord network,after\
        a failure"
        Pyro.core.initServer()
        ns=Pyro.naming.NameServerLocator().getNS()
        self._cdaemon=Pyro.core.Daemon()
        self._cdaemon.useNameServer(ns)
        
        uri=self._cdaemon.connect(self._controlClassInstance,str(self._portNumber))
        
        logging.debug("Master Process: Listening for Control messages on {0}".format(self._cdaemon.port))
        
        self._cdaemon.requestLoop()
        
    def insertFiles(self,fileInserts):
        print "Master Process:Master Process:Inserting files into Chord network."
        for i in range(fileInserts):
            for index,node in enumerate(nodeHandles):
                if nodeStatus[index]: # and node.isAlive():
                    node.insertFile("files/foo{0}".format(i))
                    cnt=0
                    for j in nodeStatus:
                        if j:
                            cnt+=1
                    if self._churn_rate > 0:
                        print "Number of live nodes {0}".format(cnt)
                    break
                
            time.sleep(0.05);
        print "Master Process: Done inserting"         
        
    def searchFiles(self,fileSearches):
        totalSteps = 0.
        searchFails = 0
        print "Master Process:Searching for files..."
        for file in range(fileSearches):
            retries = 0
            searchStatus = False
            
            if self._churn_rate > 0:
                delay = math.ceil(random.expovariate(1)*3)
                time.sleep(delay)
            
            print "Searching for file foo{0}:".format(file)            
            
            # Randomly select one node to search the file
            while retries < 5:
                index = random.randint(0,self._n_clients-1)
                if nodeStatus[index]: # nodeHandles[index].isAlive():
                    print "Master process: Searching for file foo{0} from node {1}".format(file,nodeHandles[index].getKey())
                    try:
                        (node,steps)= nodeHandles[index].searchFile("foo{0}".format(file))
                        searchStatus = True
                    except:
                        searchStatus = False
                    break
                retries += 1
                    
            if not searchStatus:
                fileSearches -=1
                continue
            
            if node ==None: 
                searchFails += 1
            totalSteps = totalSteps + steps
            
        print "Master Process: Total number of failed searches: {0} out of {1} ({2}% failure rate)".format(searchFails,fileSearches,float(searchFails)/fileSearches)
        print "Master Process: Total number of steps: {0} ({1} steps on average)".format(totalSteps,totalSteps/fileSearches)
        
    def getBootstrapNode(self):
        for node in nodeHandles:
            if node.isAlive():
                return node.getPort()
        
        logging.error("No node is alive in the Network")
        
    def notifyControl(self,port,status):
        pos = (port -  self._basePort) / 2
        if status==False:
            if self._liveNodes <= math.ceil((1-self._churn_rate)*self._n_clients):
                return False
            
        if status:
            self._liveNodes+=1
        else:
            self._liveNodes-=1
            
        nodeStatus[pos] = status
        return True
        
        
        
def main():
    
    # The number of chord processes should be given
    # as a command line argument        
    if len(sys.argv) !=3:
        sys.stderr.write("Usage: chordControl PROCS_NUMBER CHURN_RATE")
        exit()
    numberOfClients = int(sys.argv[1])
    churn = float(sys.argv[2])
    
    c = ChordControl(numberOfClients,churn)
    
    #Wait for user, in order to proceed
    sys.stdin.readline(1)
    
    fileInserts = 1000
    fileSearches = 1000
    
    # Insert files in ring
    c.insertFiles(fileInserts)
    
    # Wait until user input given
    sys.stdin.readline(1)

    c.searchFiles(fileSearches)
    
    
if  __name__ == "__main__":
    main()

    

    
    

    