
class Node:
    def __init__(self,key,val,n):
        self.key = key
        self.val = val 
        self.next = n


class SeparateChaining:
    def __init__(self,N):
        self.N = N 
        self.hashtable = [None]*N

    def getHash(self,key):
        return (hash(key) & 0x7ffffff) % self.N

    def insert(self,key,val):
        i = self.getHash(key)
        node = self.hashtable[i]

        # 일치하는 node가 있다면 값을 수정
        while node != None:
            if node.key == key:
                node.val = val
                return 
            node = node.next
        # 일치하는 node가 없다면 추가
        self.hashtable[i] = Node(key,val,self.hashtable[i])

    def get(self, key):
        i = self.getHash(key)
        node = self.hashtable[i]
        while node != None:
            if node.key == key:
                return node.val 
            node = node.next 
        return None

    def print_table(self):
        for node in self.hashtable:
            while node != None:
                print(node.key, node.val, end=" | ")
                node = node.next
            print("")


if __name__ == "__main__":
    ht = SeparateChaining(5)

    ht.insert(1, 4)
    ht.insert(2, 5)
    ht.insert(3, 6)
    ht.insert(5, 4)
    ht.insert(6, 5)
    ht.insert(7, 6)
    ht.insert(11,5)

    ht.print_table()

    print(ht.get(11))