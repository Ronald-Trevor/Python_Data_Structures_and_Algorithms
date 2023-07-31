from stack import Stack

def is_match(p1,p2):
	if p1 == '(' and p2 == ')':
		return True
	elif p1 == '{' and p2 == '}':
		return True
	elif p1 == '[' and p2 == ']':
		return True
	else:
		return False

def is_paren_match(paren_string):
	s = Stack()
	index = 0
	is_balanced = True

	while index < len(paren_string) and is_balanced:
		paren = paren_string[index]
		if paren in '({[':
			s.push(paren)
		else:
			if s.is_Empty():
				is_balanced = False
				break
			else:
				top = s.pop()
				if not is_match(top, paren):
					is_balanced = False
					break 
		index += 1

	if s.is_Empty() and is_balanced:
		return True
	else:
		return False

print(is_paren_match('((({{[]}})))'))
print(is_paren_match("{[{(}]}"))
print(is_paren_match('[][]{'))