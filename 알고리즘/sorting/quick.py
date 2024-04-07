from random import shuffle

a = [5,10,1,2,9,6,4,3,8,7]

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def sort(a):
    N = len(a)
    shuffle(a)
    _sort(a,0,N-1)
    return a 

def _sort(a,lo,hi):
    if lo >= hi:
        return
    i,j = lo+1,hi
    while True:
        while i <= hi and a[i] < a[lo]:
            i += 1
        while j >= lo+1 and a[lo] < a[j]:
            j -= 1

        if i >= j:
            break
        swap(a,i,j)
    swap(a,lo,j)

    _sort(a,lo,j-1)
    _sort(a,j+1,hi)

print(sort(a))
