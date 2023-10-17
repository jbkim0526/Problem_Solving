
from math import floor
t = int(input())
belts = None
nodes = {}
class Node:
    def __init__(self,val):
        self.next = None
        self.prev = None
        self.val = val
class Belt:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def add_tail(self,val):
        n = Node(val)
        if self.count == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.count += 1
        nodes[val] = n

    def pop_head(self):
        n = self.head
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head = n.next
            self.head.prev = None
        self.count -= 1
        return n

    def find_ith(self,n):
        cur = self.head
        for _ in range(n-1):
            cur = cur.next
        return cur

    def print(self):
        c = self.head
        before = []
        l = []
        after = []
        while c:
            before.append(c.prev.val if c.prev else None)
            l.append(c.val)
            after.append(c.next.val if c.next else None)
            c = c.next

for _ in range(t):

    line = list(map(int,input().split()))
    command = line[0]
    if command == 100:
        n,m,belt_nums = line[1],line[2],line[3:]
        belts = [None]+ [Belt() for _ in range(n)]
        for i,belt_num in enumerate(belt_nums):
            belts[belt_num].add_tail(i+1)

    elif command == 200:
        src,dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]

        # 옮길게 없으면 그대로
        if belt_src.count == 0:
            continue
        # dest가 0인경우
        if belt_dest.count == 0:
            belt_dest.head = belt_src.head
            belt_dest.tail = belt_src.tail
        else:
            belt_dest.head.prev = belt_src.tail
            belt_src.tail.next = belt_dest.head
            belt_dest.head = belt_src.head

        belt_src.head = None
        belt_src.tail = None
        belt_dest.count += belt_src.count
        belt_src.count = 0
        print(belts[dest].count)

    elif command == 300:
        src, dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]
        src2dest,dest2src = None,None
        if belt_src.count > 0:
            src2dest = belt_src.pop_head()
        if belt_dest.count > 0:
            dest2src = belt_dest.pop_head()
        if src2dest:
            belt_dest.add_tail(src2dest.val)
        if dest2src:
            belt_src.add_tail(dest2src.val)
        print(belts[dest].count)


    elif command == 400:
        src, dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]
        i = floor(belt_src.count/2)
        # src에서 안옮기면 그냥 두기
        if i == 0:
            continue
        src_node = belt_src.find_ith(i)
        src_next = src_node.next

        # dest가 비어있는 경우
        if belt_dest.count == 0:
            belt_dest.head = belt_src.head
            belt_dest.tail = src_node
            belt_src.head = src_next
            src_next.prev =None
            src_node.next = None
        else:
            # 꼬리연결
            src_node.next = belt_dest.head
            belt_dest.head.prev = src_node
            belt_dest.head = belt_src.head
            belt_src.head = src_next
            src_next.prev = None

        belt_dest.count += i
        belt_src.count -= i
        print(belts[dest].count)
    #
    elif command == 500:
        p_num = line[1]
        a = nodes[p_num].prev.val if nodes[p_num].prev else -1
        b = nodes[p_num].next.val if nodes[p_num].next else -1
        print(a+b*2)
    else:
        belt = belts[line[1]]
        if belt.count == 0:
            print(-3)
        else:
            a,b,c = belt.head.val,belt.tail.val,belt.count
            print(a+b*2+c*3)

