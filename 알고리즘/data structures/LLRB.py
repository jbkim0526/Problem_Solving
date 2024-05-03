RED = True 
BLACK = False

class Node:
    def __init__(self,key,val,color):
        self.key = key 
        self.val = val 
        self.color = color 
        self.left = None 
        self.right = None 

class LLRB_Tree:
    def __init__(self):
        self.root = None 
    
    def isRed(self, x):
        if x == None:
            return BLACK 
        return x.color == RED

    def rotateLeft(self, h):
        x = h.right 
        h.right = x.left 
        x.left = h 
        x.color = h.color 
        h.color = RED
        return x

    def rotateRight(self,h):
        x = h.left 
        h.left = x.right 
        x.right = h 
        x.color = h.color
        h.color = RED 
        return x 
    
    def flipColor(self,h):
        h.color = RED 
        h.left.color = BLACK 
        h.right.color = BLACK

    def insert(self,key,val):
        self.root = self._insert(x, key, val)

    def _insert(self,x,key,val):
        if x == None:
            return Node(key,val,RED)
        
        if val < x.val:
            x.left = self._insert(x.left, key, val)
        elif x.val < val:
            x.right = self._insert(x.right, key, val)
        else:
            x.val = val 
        
        # Check leftRotation
        if self.isRed(x.right) and not self.isRed(x.left):
            self.rotateLeft(x)

        # Check rightRotation
        if self.isRed(x.left) and self.isRed(x.left.left):
            self.rotateRight(x)
        
        # Check Flip
        if self.isRed(x.left) and self.isRed(x.right):
            self.flipColor(x)

        return x
        

        
