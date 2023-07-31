class Stack:
	def __init__(self):
		self.items = [ ]

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def get_Stack(self):
		return self.items

	def is_Empty(self):
		return self.items == [ ]

	def peek(self):
		if not self.is_Empty():
			return self.items[-1]

my_stack = Stack()
my_stack.push('A')
my_stack.push('B')
print(my_stack.get_Stack())
my_stack.push('C')
print(my_stack.get_Stack())
my_stack.pop()
print(my_stack.is_Empty())
print(my_stack.get_Stack())
print(my_stack.peek())

