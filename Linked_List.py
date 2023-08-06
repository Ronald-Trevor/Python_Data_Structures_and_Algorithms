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

	def delete_node(self, key):
		#delete head node 
		cur_node = self.head

		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			return
    #delete node which is not head node 
		prev = None 
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return

		prev.next = cur_node.next
		cur_node = None
  
	def delete_node_at_pos(self,pos):
		if self.head:
			cur_node = self.head
			if pos == 0:
				self.head = cur_node.next
				cur_node = None 
				return

			prev = None
			count = 0
			while cur_node and count != pos:
				prev = cur_node
				cur_node = cur_node.next
				count += 1

			if cur_node is None:
				return

			prev.next = cur_node.next
			cur_node = None


	def len_of_list(self):
		cur_node = self.head
		count = 0
		while cur_node:
			count += 1
			cur_node = cur_node.next

		return count

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("K")
llist.append("H")
llist.append("G")
llist.append("F")
llist.preppend("D")

print(llist.len_of_list())
llist.insert_after_node(llist.head.next,"E")

llist.delete_node("D")
llist.delete_node("C")

llist.delete_node_at_pos(2)

llist.printlist()
print(llist.len_of_list())



