from collections import defaultdict

def solution(stones, k):
    sorted_stones = []
    for i,stone in enumerate(stones):
        sorted_stones.append((stone,i))
    sorted_stones.sort()
    adj_sets = defaultdict(set)

    for stone,index in sorted_stones:
        s1 = adj_sets[index-1]
        s2 = adj_sets[index+1]
        n1 = len(s1)
        n2 = len(s2)
        if n1 > 0 and n2 > 0:
            s1.update(s2)
            s2.update(s1)
            s1.add(index)
            s2.add(index)
            adj_sets[index] = s1
        elif n1 > 0:
            s1.add(index)
            adj_sets[index] = s1 
        elif n2 > 0:
            s2.add(index)
            adj_sets[index] = s2 
        else:
            adj_sets[index].add(index)

        if len(adj_sets[index]) == k:
            return stone




print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 5))