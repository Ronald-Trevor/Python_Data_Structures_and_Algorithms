class Node:
	def __init__(self,data):
		self.data = data
		self.next = None 
		self.prev = None 

class DoublyLinkedList:
	def __init__(self):
		self.head = None 

	def append(self,data):
		if self.head is None :
			new_node = Node(data)
			self.head = new_node
		else:
			new_node = Node(data)
			cur = self.head 
			while cur.next:
				cur = cur.next
			cur.next = new_node
			new_node.prev = cur 

	def print_list(self):
		cur = self.head 
		while cur:
			print(cur.data)
			cur = cur.next 

	def preppend(self,data):
		if self.head is None:
			new_node = Node(data)
			self.head = new_node
		else:
			new_node = Node(data)
			cur = self.head
			cur.prev = new_node
			new_node.next = cur 
			self.head = new_node

	def add_after_node(self,data,key):
		cur = self.head
		while cur:
			if cur.next is None and cur.data == key:
				self.append(data)
				return 
			elif cur.data == key:
				new_node = Node(data)
				nxt = cur.next
				cur.next = new_node
				new_node.next = nxt 
				new_node.prev = cur 
				nxt.prev = new_node
				return 
			cur = cur.next 

	def add_before_node(self,data,key):
		cur = self.head 
		while cur:
			if cur.next is None and cur.data == key:
				self.preppend(data)
			elif cur.data == key :
				new_node = Node(data)
				previous = cur.prev
				previous.next = new_node 
				cur.prev = new_node
				new_node.next = cur 
				new_node.prev = previous
				return
			cur = cur.next  

	def delete_node(self,key):
		cur = self.head 
		while cur :
			#deleting only node
			if cur.data == key and cur == self.head:
				if not cur.next:
				    cur = None 
				    self.head = None 
				    return
			#deleting head node
				else:
					nxt = cur.next 
					cur.next = None 
					cur.prev = None 
					cur = None 
					self.head = nxt 
					return 
			elif cur.data == key :
				if cur.next :
					nxt = cur.next 
					prev = cur.prev 
					prev.next = nxt 
					nxt.prev = prev 
					cur.next = None 
					cur.prev = None 
					cur = None 
					return 
			cur = cur.next 

	def reverse(self):
		temp = None 
		cur = self.head 
		while cur :
			temp = cur.prev 
			cur.prev = cur.next 
			cur.next = temp 
			cur = cur.prev 
		if temp :
			self.head = temp.prev 

list1 = DoublyLinkedList()
list1.append("C")
list1.append("D")
list1.preppend("B")
list1.preppend("A")
list1.print_list()
print("\n")
list1.add_after_node("E","D")
list1.add_before_node("F","B")
list1.print_list()
list2 = DoublyLinkedList()
list2.append("G")
print("\n")
list2.print_list()
list2.delete_node("G")
list2.print_list()
print("\n")
list3 = DoublyLinkedList()
list3.append(1)
list3.append(3)
list3.append(7)
list3.append(8)
list3.append(5)
list3.print_list()
print("\n")
list3.delete_node(1)
list3.print_list()
print("\n")
list3.delete_node(7)
list3.print_list()
print("\n")
list4 = DoublyLinkedList()
list4.append(1)
list4.append(2)
list4.append(3)
list4.append(4)
list4.append(5)
list4.append(6)
list4.reverse()
list4.print_list()
