class Node:
	def __init__(self,val, n):
		self.element = val
		self.next = n

	def getElem(self):
		return self.element

	def getNext(self):
		return self.next

	def setNext(self,n):
		self.next = n
		
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def size(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def first(self):
		return self.head

	def last(self):
		return self.tail

	def addFirst(self,val):
		self.head = Node(val,self.head)
		if self.size == 0:
			self.tail = self.head
		self.size += 1

	def addLast(self,val):
		new_node = Node(val,None)
		if self.size == 0:
			self.head = new_node
		else:
			self.tail.setNext(new_node)
		self.tail = new_node
		self.size += 1
		
	def removeFirst(self):
		if self.isEmpty():
			return None
		ans = head.getElem()
		head = head.getNext()
		size -= 1
		if size == 0:
			tail == None
		return ans