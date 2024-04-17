d = [1,2,3,4,5]
n = len(d)
m = 3

# permutation without replacement
def track(res):
    if len(res) == m:
        print(res)
        return
    for num in d:
        if num in res:
            continue
        res.append(num)
        track(res)
        res.pop()

# permutation with replacement
def track(res):
    if len(res) == m:
        print(res)
        return
    for num in d:
        res.append(num)
        track(res)
        res.pop()

# 중복원소가 있는 permutation
d = [1,1,2,2,3,3,4,4,5]
n = len(d)
m = 3

# counter 생성
from collections import defaultdict
counter = defaultdict(int)
for num in d:
    counter[num] += 1

def track(res):
    if len(res) == m:
        print(res)
        return
    for num,count in counter.items():
        if count == 0:
            continue
        res.append(num) ; counter[num] -= 1
        track(res)
        res.pop() ; counter[num] += 1

track([])








