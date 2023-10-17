import sys
input = sys.stdin.readline 

n = int(input())
ans = -1
dp = [n]
flag = True
while flag:
    temp = []
    ans += 1
    for elem in dp:
        if elem == 1:
            flag = False
            break
        if elem % 2 == 0:
            temp.append(elem // 2)
        if elem % 3 == 0:
            temp.append(elem // 3)
        temp.append(elem-1)
    dp = temp
print(ans)
    

