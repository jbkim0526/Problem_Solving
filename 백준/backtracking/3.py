import sys
input = sys.stdin.readline 

N, M = map(int,input().split())
L = [str(i) for i in range(1,N+1)]

def track(l,s,d):
    if d >= M:
        print(s[1:])
        return
    for i in range(len(l)):
        news = s +' '+ l[i]
        track(l,news,d+1)

track(L,'',0)