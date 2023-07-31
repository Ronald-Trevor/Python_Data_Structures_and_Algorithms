from stack import Stack

def reverse_string(string):
	s = Stack()
	reversed = ""
	for i in range(len(string)):
		s.push(string[i])

	while not s.is_Empty():
		reversed += s.pop()

	return reversed

print(reverse_string("trevor"))