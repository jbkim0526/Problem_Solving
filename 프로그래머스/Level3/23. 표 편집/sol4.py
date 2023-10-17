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
    head = Node(-1)
    tail = Node(-1)
    prev_node = head
    target_node = None
    erased = []

    for i in range(n):
        cur_node = Node(i)
        if i == k:
            target_node = cur_node
        prev_node.next = cur_node
        cur_node.prev = prev_node 
        prev_node = cur_node

    cur_node.next = tail 
    tail.prev = cur_node

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
            next_node.prev = prev_node
            prev_node.next = next_node

            target_node = next_node if next_node != tail else prev_node
            
        else:
            restore_target = erased.pop()
            restore_target.prev.next = restore_target
            restore_target.next.prev = restore_target

    node = head.next
    while node != tail:
        answer[node.val] = "O"
        node = node.next

    return "".join(answer)






    

