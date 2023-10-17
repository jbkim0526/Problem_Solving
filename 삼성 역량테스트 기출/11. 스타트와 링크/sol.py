import sys 
from itertools import combinations
from math import inf
input = sys.stdin.readline

n = int(input()[:-1])
b = [list(map(int,input().split())) for _ in range(n)]

persons = [i for i in range(n)]
answer = inf

for t1 in combinations(persons,n//2):
    score_1 = 0
    score_2 = 0
    
    t2 = []
    for i in range(n):
        if i in t1:
            continue 
        t2.append(i) 

    for person in t1:
        for other in t1:
            if other == person:
                continue 
            score_1 += b[person][other]
    
    for person in t2:
        for other in t2:
            if other == person:
                continue 
            score_2 += b[person][other]

    answer = min(answer,abs(score_1-score_2))
    if answer == 0:
        break 

print(answer)

