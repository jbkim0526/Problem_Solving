import sys
input = sys.stdin.readline 

N, M = map(int,input().split())
L = [str(i) for i in range(1,N+1)]

def track(l,s,d):
    if len(l) == 0 or d >= M:
        print(s[1:])
        return
    for i in range(len(l)):
        temp = l.copy()
        news = s +' '+ temp.pop(i)
        track(temp,news,d+1)

track(L,'',0)

