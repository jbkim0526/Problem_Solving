from collections import deque

T = int(input())
hex_dict = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
for i in range(10):
    hex_dict[str(i)] = i
def hextodec(s):
    n = len(s)
    res = 0
    for i in range(n):
        res += hex_dict[s[i]]*(16**(n-1-i))
    return res

for _ in range(T):
    n, k = map(int,input().split())
    l = n // 4
    number_sets = set()
    box = deque(input())

    for _ in range(l):
        # 4개의 변을 잘라서 number_sets에 입력
        for i in range(4):
            edge = "".join([box[i*l+j] for j in range(l)])
            number_sets.add(hextodec(edge))
        # 1칸 회전
        box.rotate(1)
    number_list = list(number_sets)
    number_list.sort(reverse=True)
    print(number_list[k-1])