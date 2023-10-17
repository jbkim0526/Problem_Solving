from bisect import bisect_left

def solution(people, limit):
    people.sort()
    n = bisect_left(people, limit)
    answer = len(people) - n
    left = 0
    right = n-1
    while left <= right:
        if people[right] + people[left] <= limit:
            left += 1
        right -= 1 ; answer += 1
    return answer

print(solution([70, 50, 80, 50],	100))