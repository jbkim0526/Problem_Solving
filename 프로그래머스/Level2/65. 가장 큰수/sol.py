#53

from math import log10

def f(x):
    if x == 0: return (0,0,0,0)
    n = int(log10(x))
    if n == 3: return (1,0,0,-n)
    elif n == 2: return ((x//100)%10,(x//10)%10,(x//1)%10,-n)
    elif n == 1: return ((x//10)%10,(x//1)%10,(x//1)%10,-n)
    else: return (x%10, x%10, x%10,-n)

def solution(numbers):
    numbers.sort(key= f, reverse=True)
    print(numbers)
    return "".join(map(str, numbers))


print(solution([2,232,23,200,222,22,299]))
print(solution([1000,100,10,1]))