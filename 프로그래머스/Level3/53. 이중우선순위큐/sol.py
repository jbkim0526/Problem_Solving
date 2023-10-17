class Node:
    def __init__(self,val,count):
        self.val = val
        self.count = count
        self.left = None
        self.right = None
        self.parent = None 

class Tree:
    def __init__(self,val):
        self.root = Node(val,1)
        self.min_node = self.root
        self.max_node = self.root

    def add_node(self,val):
        new_node = Node(val,1)
        if val > self.max_node.val:
            self.max_node = new_node 
        if val < self.min_node.val:
            self.min_node = new_node
        cur_node = self.root
        while True:
            if val > cur_node.val:
                if cur_node.right == None:
                    cur_node.right = new_node
                    new_node.parent = cur_node
                    break
                cur_node = cur_node.right 

            elif val < cur_node.val:
                if cur_node.left == None:
                    cur_node.left = new_node
                    new_node.parent = cur_node
                    break
                cur_node = cur_node.left 
            else:
                cur_node.count += 1
                break
    

    def min_node_in_subtree(self,node):
        if node.left == None:
            return node 
        return min_node_in_subtree(node.left)


    def remove_min_node(self):
        if self.min_node.count > 1:
            self.min_node.count -= 1
        else:
            self.min_node.parent.left = self.min_node.right
            if self.min_node.right:
                self.min_node.right.parent = self.min_node.parent
                self.min_node = self.min_node_in_subtree(self.min_node.right)
            else:
                self.min_node = self.min_node.parent
    
    def printtree(self):
        self._printtree(self.root)
    
    def _printtree(self,cur_node):
        if cur_node == None:
            return 
        print(cur_node.val)
        self._printtree(cur_node.left)
        self._printtree(cur_node.right)
    


        
def solution(operations):
    answer = []
    
    #tree = Tree(int(operations[0][2:]))
    tree = Tree(1)
    tree.add_node(3)
    tree.add_node(4)
    tree.add_node(2)
    tree.add_node(5)
    tree.add_node(6)
    tree.printtree()
    tree.remove_min_node()
    tree.printtree()
    print(tree.min_node.val)
    
    
    
    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    
