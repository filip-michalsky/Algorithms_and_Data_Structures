
class Node():
    
    def __init__(self,value,next_pointer,min_val):
        self.value = value
        self.next = next_pointer
        self.min = min_val

class MinStack():

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.nodes = None
		self.head = None
		self.next = None

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""

		if type(x) != int:
			raise ValueError('The input value needs to be an integer!')
		
		# first, handle the case when we have an empty stack
		if self.head == None:
			new_node = Node(x,self.next,x)
			self.nodes = [new_node]
			self.head = new_node

		# now handle the case when we do not have an empty stack
		else:
			if x < self.head.min:
				min_val = x
			else:
				min_val = self.head.min

			self.next = self.head

			new_node = Node(x,self.next,min_val)

			self.head = new_node

			self.nodes = [new_node] + self.nodes

	def pop(self):
		"""
		:rtype: void
		"""

		if self.head == None:
			raise ValueError('Cannot pop an element from an empty stack!')

		# reassign head node
		self.head = self.next

		

		# reassign the pointer to the next node
		# if we are at the last node:
		if len(self.nodes)==1:
			self.next = None
		else:
			self.next = self.next.next
			# pop the first node from the list of nodes
			self.nodes = self.nodes[1:]

	def top(self):
		"""
		:rtype: int
		"""

		return self.head.value

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.head.min

stack = MinStack()


stack.push(5)
stack.push(4)
stack.push(3)

print(stack.top())
print(stack.getMin())
print('-'*40)
stack.pop()
print(stack.top())