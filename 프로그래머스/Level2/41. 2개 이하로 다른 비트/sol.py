def count1(x):
    t = x % 2
    count = 0
    while t == 1:
        count += 1
        x //= 2
        t = x % 2
    return count

def solution(numbers):
    answer = []
    for number in numbers:
        if number & 0: 
            answer.append(number + 1)
            continue
        c1 = count1(number)
        if c1 <= 1:
            answer.append(number + 1)
        else:
            answer.append(number + 2**(c1-1))
    return answer

print(count1(11))
print(solution([2,7]))

