from itertools import combinations


a = [(1,0),(3,0),(5,0),(2,0),(4,0)]

for c in combinations(a,3):
    print(c)