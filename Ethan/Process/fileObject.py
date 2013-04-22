class fileObject:
    "This object represents a file, since Pyro does not\
    allow to pass files between processes"
    def __init__(self,fileName,hashKey = None):
        
        # Create an open file object from the fileName
        file = open(fileName,'a+')
        self._filename = fileName
        
        self._fileData = file.readlines()
        file.close()
        
        # Find the hash key for the file
        self._fileKey = hashKey
    
    def getName(self):
        return self._filename
    
    def getData(self):
        return self._fileData
    
    def getKey(self):
        return self._fileKey

