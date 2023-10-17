import sys
input = sys.stdin.readline 

N, M = map(int,input().split())
L = [str(i) for i in range(1,N+1)]

def track(l,s,d):
    if d >= M:
        print(s[1:])
        return
    temp = l.copy()
    for i in range(len(l)):
        news = s +' '+ temp[0]
        track(temp,news,d+1)
        temp.pop(0)

track(L,'',0)
