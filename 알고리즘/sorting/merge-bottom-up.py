a = [5,10,1,2,9,6,4,3,8,7]

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def merge(a,lo,mid,hi):
    i,j = lo, mid+1
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
    
    for i in range(lo,hi+1):
        a[i] = aux[i-lo]


def sort(a):
    N = len(a)
    size = 1

    # 크기가 size인 두 구간을 merge
    while size < N:
        # lo: 시작위치 N-size 보다 작아야 왼쪽구간을 포함하여 merge가 가능
        for lo in range(0,N-size,2*size):
            mid, hi = lo+size-1, min(lo+2*size-1,N-1)
            merge(a,lo,mid,hi)
        size *= 2
    return a 

print(sort(a))