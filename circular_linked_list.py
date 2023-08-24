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

	def __len__(self):
		count = 0
		cur = self.head 
		while cur:
			count += 1
			cur = cur.next 
			if cur == self.head:
				break 
		return count

	def split_list(self):
		size = len(self)
		if size == 0:
			return None 
		if size == 1:
			return self.head

		mid = size//2
		count = 0

		cur = self.head 
		prev = None 
		while cur and count < mid:
			count += 1
			prev = cur 
			cur = cur.next
		prev.next = self.head 

		split_list = CircularLinkedList()
		while cur.next != self.head:
			split_list.append(cur.data)
			cur = cur.next
		split_list.append(cur.data)

		self.print_list()
		print("\n")
		split_list.print_list()

	def remove_node(self,node):
		if self.head:
			if self.head == node:
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
					if cur == node:
						prev.next = cur.next 
						cur = cur.next

	def josephus_problem(self,step):
		cur = self.head
		length = len(self)
		while length > 1:
			count = 1
			while count != step:
				cur = cur.next
				count += 1
			print("KILL" + str(cur.data))
			self.remove_node(cur)
			cur = cur.next
			length -= 1 


list1 = CircularLinkedList()
list1.append("C")
list1.append("D")
list1.preppend("B")
list1.preppend("A")
list1.print_list()
print("\n")
list1.remove("C")
list1.print_list()
print("\n")
llist = CircularLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")

llist.split_list()
print("\n")
list2 = CircularLinkedList()
list2.append("A")
list2.append("B")
list2.append("C")
list2.append("D")
list2.josephus_problem(2)
list2.print_list()