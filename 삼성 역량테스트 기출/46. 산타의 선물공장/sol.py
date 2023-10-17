import sys
from collections import deque
from math import floor
t = int(input())
belt_contains = []
input = sys.stdin.readline
belts = None

for _ in range(t):

    line = list(map(int,input().split()))
    command = line[0]

    if command == 100:
        n,m,belt_nums = line[1],line[2],line[3:]
        belts = [None]+ [deque() for _ in range(n)]
        belt_contains = [None] + [set() for _ in range(n)]
        for i,belt_num in enumerate(belt_nums):
            belts[belt_num].append(i+1)
            belt_contains[belt_num].add(i+1)

    elif command == 200:
        src,dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]
        # 더 작은 것을 기준으로 옮김
        if len(belt_src) < len(belt_dest):
            while belt_src:
                belt_dest.appendleft(belt_src.pop())
        else:
            while belt_dest:
                belt_src.append(belt_dest.popleft())
            belts[dest] = belt_src
            belts[src] = belt_dest
        belt_contains[dest] = belt_contains[dest] | belt_contains[src]
        belt_contains[src] = set()
        print(len(belts[dest]))

    elif command == 300:
        src, dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]
        src2dest,dest2src = None,None
        if belt_src:
            src2dest = belt_src.popleft()
        if belt_dest:
            dest2src = belt_dest.popleft()
        if src2dest:
            belt_dest.appendleft(src2dest)
            belt_contains[src].remove(src2dest)
            belt_contains[dest].add(src2dest)
        if dest2src:
            belt_src.appendleft(dest2src)
            belt_contains[dest].remove(dest2src)
            belt_contains[src].add(dest2src)
        print(len(belts[dest]))


    elif command == 400:
        src, dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]
        move_cnt = floor(len(belt_src)/2)
        temp = deque()
        temp_contains = set()
        while move_cnt > 0:
            v = belt_src.popleft()
            temp.append(v)
            temp_contains.add(v)
            move_cnt -= 1

        # 옮길게 더 적은 경우
        if move_cnt < len(belt_dest):
            while temp:
                belt_dest.appendleft(temp.pop())
        else:
            while belt_dest:
                temp.append(belt_dest.popleft())
            belts[dest] = temp

        belt_contains[src] = belt_contains[src] - temp_contains
        belt_contains[dest] = belt_contains[dest] | temp_contains
        print(len(belts[dest]))

    elif command == 500:
        p_num = line[1]

        for i in range(1,n+1):
            belt = belts[i]
            if not belt or (p_num not in belt_contains[i]):
                continue
            belt.append(-1); belt.appendleft(-1)
            for i, num in enumerate(belt):
                if num == p_num:
                    a = belt[i-1]
                    b = belt[i+1]
                    belt.pop(); belt.popleft()
                    print(a+2*b)
                    break
            break
    else:
        belt = belts[line[1]]
        if not belt:
            print(-3)
        else:
            a,b,c = belt[0],belt[-1],len(belt)
            print(a+b*2+c*3)
