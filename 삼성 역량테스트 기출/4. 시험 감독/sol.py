import sys 

input = sys.stdin.readline

n = int(input())
peoples = list(map(int,input().split()))
b,c = map(int, input().split())

ans = 0

for people in peoples:
    if people > b:
        ans += (people-b)//c + (1 if (people-b) % c else 0)
    ans += 1
print(ans)