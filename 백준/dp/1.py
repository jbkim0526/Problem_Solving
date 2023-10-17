n = int(input())

def fib(n):
    if (n ==1 or n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib2(n):
    r = 0
    f = [0]*(n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3,n+1):
       r = r + 1
    return r

print(str(fib(n)) + ' '+ str(fib2(n)))