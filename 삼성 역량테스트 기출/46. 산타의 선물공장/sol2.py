from collections import deque
from math import floor
t = int(input())

belts = None


# belt에 v 추가 (벨트는 이미 정렬 가정)
def queue_add(belt,v):
    temp = deque()
    while belt:
        # 가장 앞이 v보다 크거나 같으면 그만
        if belt[0] >= v:
            break
        # v보다 작으면
        temp.append((belt.popleft()))
    belt.appendleft(v)
    while temp:
        belt.appendleft(temp.pop())

# # 두개중 작은거부터 빼서 new에 append
# def queue_merge(belt_src,belt_dest):
#     new_belt = deque()
#     # 둘다 있는 경우
#     while belt_src and belt_dest:
#         if belt_src[0] < belt_dest[0]:
#             new_belt.append(belt_src.popleft())
#         else:
#             new_belt.append(belt_dest.popleft())
#     # 둘중 하나만 남은 이제
#     while belt_src : new_belt.append(belt_src.popleft())
#     while belt_dest: new_belt.append(belt_dest.popleft())
#     return new_belt

def queue_merge(belt_src,belt_dest):
    while belt_src:
        belt_dest.appendleft(belt_src.pop())

for _ in range(t):

    line = list(map(int,input().split()))
    command = line[0]

    if command == 100:
        n,m,belt_nums = line[1],line[2],line[3:]
        belts = [None]+ [deque() for _ in range(n)]
        for i,belt_num in enumerate(belt_nums):
            belts[belt_num].append(i+1)
            #queue_add(belts[belt_num],i+1)

    elif command == 200:
        src,dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]
        queue_merge(belt_src,belt_dest)
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
        if dest2src:
            belt_src.appendleft(dest2src)
        print(len(belts[dest]))

    elif command == 400:
        src, dest = line[1:]
        belt_src, belt_dest = belts[src], belts[dest]
        move_cnt = floor(len(belt_src)/2)
        temp = deque()
        while move_cnt >0:
            temp.append(belt_src.popleft())
            move_cnt-=1
        while temp:
            belt_dest.appendleft(temp.pop())

        # belts[src] = deque(list(belt_src)[move_cnt:])
        # queue_merge(deque(list(belt_src)[:move_cnt]),belt_dest)
        print(len(belts[dest]))

    elif command == 500:
        p_num = line[1]
        for belt in belts:
            if not belt or not p_num in belt:
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

    #print(belts)