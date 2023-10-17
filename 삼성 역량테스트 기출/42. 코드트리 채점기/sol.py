import sys
from collections import deque
from bisect import bisect_right
input = sys.stdin.readline

start_end = {}
workers = None
waiting = []
in_progress = set()
for _ in range(int(input())):

    line = input().split()
    command = line[0]

    if command =="100":
        n,(domain,id) = int(line[1]),line[2].split("/")
        waiting.append((1,(domain,id)))
        workers = [None]*n

    elif command == "200":
        t,p,(domain,id) = int(line[1]),int(line[2]),line[3].split("/")
        for elem in waiting:
            if (domain,id) == elem[1]:
                break
        else:
            i = bisect_right(waiting,(p,(domain,id)))
            waiting.insert(i,(p,(domain,id)))

    elif command == "300":
        t = int(line[1])
        # 쉬는 게 없으면 무시
        if not None in workers:
            continue
        for (p,(domain,id)) in waiting:

            # 현재 task에 대해, 채점을 진행중인 도메인지 확인
            if domain in in_progress:
                continue

            # 현재 task에 대해, 부적절한 채점인지 확인
            if domain in start_end:
                start_t,gap =start_end[domain]
                if t < start_t + 3*gap:
                    continue
            # 가능한 task가 있으면
            i = workers.index(None)
            workers[i] = (t,domain)
            waiting.remove((p,(domain,id)))
            in_progress.add(domain)
            break

    elif command == "400":
        t,i = int(line[1]),int(line[2])
        if not workers[i-1]:
            continue
        start_t,domain = workers[i-1]
        start_end[domain] = start_t,t-start_t
        in_progress.remove(domain)
        workers[i-1] = None
    else:
        print(len(waiting))
