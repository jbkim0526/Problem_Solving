#93
from math import log10

def f(x):
    if x == 0: return (0,0,0,0)
    n = int(log10(x))
    if n == 3: return (1,0,0,0)
    elif n == 2: return ((x//100)%10,(x//10)%10,(x)%10,(x//100)%10)
    elif n == 1: return ((x//10)%10,(x)%10,(x//10)%10,(x)%10)
    else: return (x%10,x%10,x%10,x%10)

def solution(numbers):
    numbers.sort(key= f, reverse=True)
    if numbers[0] == 0: return "0"
    return "".join(map(str, numbers))


print(solution([0,0,0,0]))
print(solution([1000,100,10,1]))