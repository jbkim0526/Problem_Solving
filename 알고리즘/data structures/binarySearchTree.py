class Node:

    def __init__(self,val,n):
        self.val = val
        self.left = None 
        self.right = None 
        self.n = n 

class BinarySearchTree:
    
    def __init__(self):
        self.root = None 

    def insert(self,val):
        self.root = self._insert(self.root,val)

    def _insert(self, x, val):
        if x == None:
            return Node(val, 1)
        if val < x.val:
            x.left = self._insert(x.left,val)
        elif val > x.val:
            x.right = self._insert(x.right,val)
        else:
            x.val = val 
        x.n = self.size(x.left) + self.size(x.right) + 1
        return x

    def delete(self,val):
        self.root = self._delete(self.root,val)


    def _deleteMin(self,x):
        if x.left == None:
            return x.right
        x.left = self._delete(x.left, val)
        x.n = self.size(x.left)+self.size(x.right) + 1
        return x

    def _min(self,x):
        if x.left == None:
            return x.val
        return self._min(x.left)

    def _delete(self,x,val):
        if x == None:
            return None 

        if val < x.val:
            x.left = self._delete(x.left, val)
        elif val > x.val:
            x.right = self._delete(x.right, val)
        else:
            if x.left == None:
                return x.right 
            elif x.right == None:
                return x.left
            else:
                t = x 
                x.val = self._min(x,right)
                x.right = deleteMin(t.right)
                x.left = t.left

        x.n = self.size(x.left) + self.size(x.right) + 1
        
        return x

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self,x):
        if x == None:
            return 
        self._traverse(x.left)
        print(x.val, x.n)
        self._traverse(x.right)


    def size(self,x):
        return 0 if x == None else x.n


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(3)
    bst.insert(2)
    bst.insert(5)
    bst.insert(6)
    bst.insert(1)
    print("bst insertion complete")
    bst.traverse()

    bst.delete(1)
    bst.delete(2)
    bst.delete(6)
    print("bst deletion complete")
    bst.traverse()
