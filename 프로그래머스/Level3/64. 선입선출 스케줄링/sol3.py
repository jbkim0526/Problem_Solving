from heapq import heappush,heappop

def solution(n, cores):
    heap = []
    cores_len = len(cores)
    if n <= cores_len:
        return cores[n-1]

    for i in range(cores_len):
        heappush(heap,(cores[i],i))
    n -= cores_len

    while n > 0:
        endtime, i = heappop(heap)
        heappush(heap,(endtime+cores[i],i))
        n -= 1

    return i+1

print(solution(	12, [3, 2, 1, 4, 5]))