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

	#Swapping two nodes based on their values 
	def swap_nodes(self,key1,key2):
		if key1 == key2:
			return

		prev1 = None 
		cur1 = self.head
		while cur1 and cur1.data != key1:
			prev1 = cur1
			cur1 = cur1.next

		prev2 = None 
		cur2 = self.head 
		while cur2 and cur2.data != key2:
			prev2 = cur2 
			cur2 = cur2.next

		if not cur1 or not cur2:
			return

		if prev1 :
			prev1.next = cur2
		else:
			self.head = cur2

		if prev2 :
			prev2.next = cur1
		else:
			self.head = cur1

		cur1.next,cur2.next = cur2.next,cur1.next

	# Reversing nodes of a linked list
	def reverse_nodes(self):
		prev = None 
		cur = self.head

		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt 
		self.head = prev


	def merge_lists(self, list1):
		p = self.head
		q = list1.head
		s = None 

		if not p:
			return q
		if not q:
			return p 
		if p and q:
			if p.data <= q.data:
				s= p
				p = s.next
			else:
				s = q
				q = s.next
			new_head = s  

		while p and q:
			if p.data <= q.data:
				s.next = p 
				s = p 
				p = s.next
			else:
				s.next = q
				s= q
				q = s.next
		if not p:
			s.next = q 
		if not q:
			s.next = p 

		self.head = new_head
		return self.head 
	def remove_duplicates(self):
		prev = None 
		cur = self.head
		duplicates = dict()

		while cur:
			if cur.data in duplicates:
				prev.next = cur.next
				cur = None 
			else:
				duplicates[cur.data] = 1
				prev = cur 
			cur = prev.next


	def nth_node(self,n):
		total_length = self.len_of_list()
		cur = self.head
		while cur :
			if total_length == n:
				print(cur.data)
				return cur.data
			total_length -= 1 
			cur = cur.next
		if cur is None :
			return 


	def count_occurences(self,data):
		count = 0
		cur = self.head 
		while cur :
			if cur.data == data:
				count += 1
			cur = cur.next
		return count 

	def rotate(self,k):
		if self.head and self.head.next :
			p = self.head 
			q = self.head 
			prev = None 
			count = 0

			while p and count < k:
				prev = p 
				p = p.next 
				q = q.next 
				count += 1
			p = prev  
			while q :
				prev = q
				q = q.next 
			q = prev 
			q.next = self.head
			self.head = p.next  
			p.next = None 
	def is_palindrome(self):
		s =" "
		p = self.head 
		while p:
			s += p.data
			p = p.next
		return s == s[::-1]


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("K")
llist.append("H")
llist.append("G")
llist.append("F")
llist.preppend("D")
llist.printlist()
print(llist.is_palindrome())
print("\n")

llist.swap_nodes("C","F")
llist.printlist()
print(llist.len_of_list())

llist.insert_after_node(llist.head.next,"E")

print("\n")

llist.delete_node("D")
llist.delete_node("C")

llist.delete_node_at_pos(2)

print("\n")

llist.printlist()
print(llist.len_of_list())

print("\n")

llist.reverse_nodes()
llist.printlist()
list1 = LinkedList()
list2 = LinkedList()
list1.append(1)
list1.append(5)
list1.append(7)
list1.append(9)
list1.append(10)

list2.append(2)
list2.append(3)
list2.append(4)
list2.append(6)
list2.append(8)

print("\n")
list1.printlist()
print("\n")
list2.printlist()
print('\n')
list1.merge_lists(list2)
list1.printlist()
print("\n")
list3 = LinkedList()
list3.append(1)
list3.append(6)
list3.append(2)
list3.append(2)
list3.append(4)
list3.append(1)
list3.rotate(3)
list3.printlist()
print("\n")
print(list3.count_occurences(2))
print("\n")
list3.remove_duplicates()
list3.printlist()
print("\n Nth node os list 3")
list3.nth_node(3)
