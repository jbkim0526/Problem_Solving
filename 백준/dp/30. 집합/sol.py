import sys 
input = sys.stdin.readline 

s = set()

for _ in range(int(input())):
    
    l = input().split()
    op = l[0]
    if op == "add":
        x = int(l[1])
        s.add(x)
    elif op == "remove":
        x = int(l[1])
        if x in s:
            s.remove(x)
    elif op == "check":
        x = int(l[1])
        print(1 if x in s else 0)
    elif op == "toggle":
        x = int(l[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif op == "all":
        s = set([i for i in range(1,21)])
    else:
        s = set()
