from collections import deque


def equalPartition(self, N, arr):
    # code here
    arr_sum = sum(arr)
    
    if arr_sum % 2:
        return 0
    target = arr_sum // 2
    dp = [set() for _ in range(N+1)]

    for i in range(1,N+1):
        num = arr[i-1]
        for elem in dp[i-1]:
            if num+elem < target:
                dp[i].add(num+elem)
            if num+elem == target:
                return 1
            dp[i].add(elem)
        if num == target:
            return 1
        dp[i].add(num)
    return 0