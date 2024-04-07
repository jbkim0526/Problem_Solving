a = [5,10,1,2,9,6,4,3,8,7]

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def sink(a, i, N):
    # left child라도 있는 경우 계속실행
    while 2*i+1 < N:
        child = 2*i+1
        # right child가 있고 left 보다 큰 경우 right을 선택
        if child+1 < N and a[child] < a[child+1]:
            child += 1
        if a[i] > a[child]:
            break 
        swap(a,i,child)
        i = child


def create_max_heap(a,N):
    for i in range(N//2,-1,-1):
        sink(a,i,N)
    

def sort(a):
    N = len(a)
    
    ### CREATE MAX HEAP
    create_max_heap(a,N)

    ### sort
    for i in range(N-1,-1,-1):
        swap(a,0,i)
        sink(a,0,i)
    
    return a 

print(sort(a))