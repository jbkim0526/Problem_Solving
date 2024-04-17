class LinearProbingHash:

    def __init__(self, N):
        self.N = N
        self.keys = [None]*N
        self.values = [None]*N 

    
    def getHash(self,key):
        return (hash(key) & 0x7fffffff) % self.N 
    
    def put(self,key,value):
        i = self.getHash(key)
        # 빈칸을 찾거나, 같은 값을 찾을 때 까지 진행
        while self.keys[i] != None:
            if self.keys[i] == key:
                self.values[i] = value 
                return
            i  = (i+1) % self.N 
        
        key[i] = key 
        vals[i] = val 
    
    def get(self,key,value):
        i = self.getHash(key)
        # 빈칸에 도달하거나, 같은 값을 찾을 때 까지 진행
        while self.keys[i] != None:
            if self.keys[i] == key:
                return self.values[i]
            i  = (i+1) % self.N 
        return None
