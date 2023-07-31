from stack import Stack

def convert_to_binary(dec_num):
	s = Stack()
	binary = ""
	while dec_num > 0 :
		s.push(str(dec_num%2))
		dec_num = dec_num//2

	while not s.is_Empty():
		binary += s.pop()

	return binary 

print(convert_to_binary(242))