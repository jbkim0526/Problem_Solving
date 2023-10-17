import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self,x,val):
        self.x = x 
        self.val = val
        self.left = None
        self.right = None

def preNode(cur_node):
    ans = []
    if not cur_node:
        return ans
    ans.append(cur_node.val+1)
    ans += preNode(cur_node.left)
    ans += preNode(cur_node.right)
    return ans

def postNode(cur_node):
    ans = []
    if not cur_node:
        return ans
    ans += postNode(cur_node.left)
    ans += postNode(cur_node.right)
    ans.append(cur_node.val+1)
    return ans
    
def solution(nodeinfos):
    sorted_nodeinfos = sorted(nodeinfos,key = lambda x: -x[1])
    root_nodeinfo = sorted_nodeinfos[0]
    root = Node(root_nodeinfo[0],nodeinfos.index(root_nodeinfo))

    for i in range(1,len(sorted_nodeinfos)):
        nodeinfo = sorted_nodeinfos[i]
        x,val= nodeinfo[0],nodeinfos.index(nodeinfo)
        target_node = Node(x,val)
        cur_node = root 
        while cur_node != target_node:
            if x < cur_node.x:
                if not cur_node.left:
                    cur_node.left = target_node
                cur_node = cur_node.left 
            elif x > cur_node.x:
                if not cur_node.right:
                    cur_node.right = target_node
                cur_node = cur_node.right
       
    return [preNode(root),postNode(root)]



print(solution([[5, 3]]))