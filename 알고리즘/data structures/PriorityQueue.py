def swap(a,i,j):
    a[i],a[j] = a[j],a[i]


class PriorityQueue:

    def __init__(self):
        self.pq = []
        self.N = 0

    def swim(self,i):
        while i > 0:
            parent = (i-1) // 2 
            # parent가 child보다 작다면
            if self.pq[i] > self.pq[parent]:
                break 
            swap(self.pq,parent,i)
            i = parent

    def sink(self,j):
        while 2*j + 1 < self.N:
            child = 2*j+1
            if child + 1 < self.N and self.pq[child] > self.pq[child+1]:
                child += 1
            # parent가 child보다 작다면
            if self.pq[child] > self.pq[j]:
                break 
            swap(self.pq,child,j)
            j = child


    def insert(self,val):
        self.pq.append(val)
        self.N += 1
        self.swim(self.N-1)

    def getMin(self):
        return self.pq[0]

    def deleteMin(self):
        swap(self.pq,0,self.N-1)
        self.N -= 1
        self.sink(0)
        return self.pq.pop()

    def isEmpty(self):
        return self.N == 0


from random import shuffle

if __name__ == "__main__":
    pq = PriorityQueue()

    a = [i for i in range(10)]
    shuffle(a)
    for num in a:
        pq.insert(num)
    
    for i in range(10):
        print(pq.deleteMin())