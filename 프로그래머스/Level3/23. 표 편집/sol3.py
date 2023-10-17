def print_list(node):
    s = ""
    while True:
        s += str(node.val)
        if node.next == None:
            break 
        node = node.next
    print(s)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.prev = None

def solution(n, k, cmd):
    answer = ["X"]*n
    head = Node(0)
    prev_node = head
    target_node = None
    erased = []

    for i in range(1,n):
        cur_node = Node(i)
        if i == k:
            target_node = cur_node
        prev_node.next = cur_node
        cur_node.prev = prev_node 
        prev_node = cur_node

    for c in cmd:
        l = c.split(" ")
        op = l[0]
        if op == "U":
            for _ in range(int(l[1])):
                target_node = target_node.prev

        elif op == "D":
            for _ in range(int(l[1])):
                target_node = target_node.next

        elif op == "C":
            erased.append(target_node)
            next_node = target_node.next 
            prev_node = target_node.prev 
            if next_node:
                next_node.prev = prev_node
                target_node = next_node
            else:
                target_node = prev_node
            if prev_node:
                prev_node.next = next_node
            
        else:
            restore_target = erased.pop()
            restore_target.prev.next = restore_target
            next_node = restore_target.next
            if next_node != None:
                next_node.prev = restore_target 

        print_list(head)
    node = head
    while True:
        answer[node.val] = "O"
        if node.next == None:
            break 
        node = node.next

    return "".join(answer)

#print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,0,["C","C","C","C","C","Z","Z"]))




    

