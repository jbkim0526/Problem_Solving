a = [5,10,1,2,9,6,4,3,8,7]

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

def sort(a):
    N = len(a)

    # a[i]를 왼쪽구간의 적절한 위치에 insert
    for i in range(1,N): 
        for j in range(i,0,-1):
            if a[j-1] > a[j]:
                swap(a,j-1,j) 

    return a 

print(sort(a))