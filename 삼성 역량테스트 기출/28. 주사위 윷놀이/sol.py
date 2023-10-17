import sys 
input = sys.stdin.readline 

class node:
    def __init__(self,val):
        self.val = val 
        self.next_node_at_start = None
        self.next_node = None 

nums = [13,16,19,22,24,28,27,26,25,30,35]
edge = {21:22,22:23,23:29,24:25,25:29,26:27,27:28,28:29,29:30,30:31,31:20}
blue_edge = {5:21,10:24,15:26}

class board:
    def __init__(self):
        self.start = node(0)
        self.end = node(0)
        self.nodes = [self.start]
        for i in range(1,21):
            new_node = node(i*2)
            self.nodes[-1].next_node = new_node
            self.nodes[-1].next_node_at_start = new_node
            self.nodes.append(new_node)
        for num in nums:
            self.nodes.append(node(num))
        for s,e in edge.items():
            self.nodes[s].next_node = self.nodes[e]
            self.nodes[s].next_node_at_start = self.nodes[e]
        for s,e in blue_edge.items():
            self.nodes[s].next_node_at_start = self.nodes[e]
            
        self.nodes[20].next_node = self.end 
        self.nodes[20].next_node_at_start = self.end 
        # 이거만 바뀜
        self.knights = [self.start, self.start, self.start, self.start]

    def move(self, i, n):
        cur_node = self.knights[i]
        if cur_node == self.end:
            return 0
        cur_node = cur_node.next_node_at_start
        for _ in range(n-1):
            # 아에 못가는 경우 -> 끝에 도착. 
            if cur_node == None or cur_node.next_node == None:
                self.knights[i] = self.end
                return 0
            cur_node = cur_node.next_node
        # 도착한 곳이 없는 경우 -> 끝에 도착.
        if cur_node == None :
            self.knights[i] = self.end
            return 0
        # 도착이 아닌 곳에 이미 말이 있는경우 -> 불가능
        if cur_node != self.end and cur_node in self.knights:
            return -1
        self.knights[i] = cur_node
        return cur_node.val

    def printknights(self):
        for k in self.knights:
            print(k.val)

b= board()
moves = list(map(int,input().split()))

def track(depth,res):
    if depth == 10:
        return res 
    ans = -1
    for i in range(4):
        cur_knights = b.knights.copy()
        v = b.move(i,moves[depth])
        ans = max(ans,track(depth+1,res+v))
        b.knights = cur_knights
    return ans

print(track(0,0))





        





    
