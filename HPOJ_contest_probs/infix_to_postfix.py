class Conversion:
	
	def __init__(self):
		self.top = -1
		self.s1 = []
		self.s2 = []
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
	
	def isEmpty(self):
		return True if self.top == -1 else False
	
	def peek(self):
		return self.s1[-1]
	
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.s1.pop()
	
	def push(self, op):
		self.top += 1
		self.s1.append(op)

	def checkprecedence(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return (a <= b)
		except KeyError:
			return False
			
	
	def infixToPostfix(self, expr):
		
		for char in expr:
		    
			if char.isalpha():
				self.s2.append(char)
			
			elif char == '(':
				self.push(char)

			elif char == ')':
				while( (not self.isEmpty()) and	self.peek() != '('):
					a = self.pop()
					self.s2.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()
					
			else:
				while(not self.isEmpty() and self.checkprecedence(char)):
					self.s2.append(self.pop())
				self.push(char)

		while not self.isEmpty():
			self.s2.append(self.pop())

		print ("".join(self.s2))

def main():
    inputs=int(input())
    while inputs>0:
        arr =input()
        obj = Conversion()
        obj.infixToPostfix(arr)
        inputs-=1
        
if __name__ == '__main__':
    main()
