a = [5,10,1,2,9,6,4,3,8,7]

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def sort(a):
    N = len(a)
    _sort(a, 0, N-1)
    return a

def merge(a,lo,mid,hi):
    i,j = lo,mid+1
    aux = []

    while i <= mid and j <= hi:
        if a[i] < a[j]:
            aux.append(a[i])
            i += 1
        else:
            aux.append(a[j])
            j += 1

    while i <= mid:
        aux.append(a[i])
        i += 1

    while j <= hi:
        aux.append(a[j])
        j += 1

    for k in range(lo,hi+1):
        a[k] = aux[k-lo]


def _sort(a, lo, hi):
    if lo >= hi:
        return 

    mid = (hi+lo)//2
    _sort(a,lo,mid)
    _sort(a,mid+1,hi)
    merge(a,lo,mid,hi)


print(sort(a))