class Node:
	def __init__(self,data):
		self.data = data
		self.next = None 

class CircularLinkedList:
	def __init__(self):
		self.head = None

	def append(self,data):
		if not self.head:
			self.head = Node(data)
			self.head.next = self.head
		else:
			new_node = Node(data)
			cur = self.head
			while cur.next != self.head:
				cur = cur.next
			cur.next = new_node
			new_node.next = self.head

	def print_list(self):
		cur = self.head
		while cur :
			print(cur.data)
			cur = cur.next
			if cur == self.head:
				break

	def preppend(self,data):
		new_node = Node(data)
		cur = self.head
		new_node.next = self.head

		if not self.head:
			new_node.next = self.head
		else:
			while cur.next != self.head:
				cur = cur.next 
			cur.next = new_node
		self.head = new_node

	def remove(self,key):
		if self.head:
			if self.head.data == key:
				cur = self.head
				while cur.next != self.head :
					cur = cur.next 
				if self.head == self.head.next :
					self.head = None 
				else:
					cur.next = self.head.next
					self.head = self.head.next
			else:
				cur = self.head 
				prev = None 
				while cur.next != self.head:
					prev = cur
					cur = cur.next 
					if cur.data == key:
						prev.next = cur.next 
						cur = cur.next


list1 = CircularLinkedList()
list1.append("C")
list1.append("D")
list1.preppend("B")
list1.preppend("A")
list1.print_list()
print("\n")
list1.remove("C")
list1.print_list()
