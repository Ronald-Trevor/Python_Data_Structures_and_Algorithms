class Node :
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printlist(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data)
			cur_node = cur_node.next

	def append(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def preppend(self,data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self,previous_node,data):
		if not previous_node:
			print("Previous Node does not exist")
			return
		new_node = Node(data)

		new_node.next = previous_node.next
		previous_node.next = new_node

	

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.preppend("D")

llist.insert_after_node(llist.head.next,"E")

llist.printlist()



