def track(numbers, target, current_val, rest_sum):
    n = len(numbers)
    ans = 0
    if n == 0:
        ans = 1 if current_val == target else 0
    else:
        num = numbers[0]
        rest_sum -= num 
        if current_val + num - rest_sum <= target :
            ans += track(numbers[1:].copy(), target, current_val + num, rest_sum)
        if current_val - num + rest_sum >= target:
            ans += track(numbers[1:].copy(), target, current_val - num, rest_sum)
    return ans

def solution(numbers, target):
    return track(numbers, target,0,sum(numbers))

print(solution([1, 1, 1, 1, 1]	,3))