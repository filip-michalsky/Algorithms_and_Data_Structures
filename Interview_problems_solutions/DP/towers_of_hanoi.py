class Node():
    
    def __init__(self,value,next_pointer):
        self.value = value
        self.next = next_pointer

class TowerHannoi():

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
			new_node = Node(x,self.next)
			self.nodes = [new_node]
			self.head = new_node

		# now handle the case when we do not have an empty stack
		else:
			if x < self.head.value:
				self.next = self.head

				new_node = Node(x,self.next)

				self.head = new_node

				self.nodes = [new_node] + self.nodes
			else:
				raise ValueError("Cannot put a bigger disk on top of smaller one in Hanoi Towers")

	def pop(self):
		"""
		:rtype: void
		"""

		if self.head == None:
			raise ValueError('Cannot pop an element from an empty stack!')

		top_val = self.head.value
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
		return top_val

	def top(self):
		return self.head.value

	@staticmethod 
	def display_towers(tower1,tower2,tower3):
		print("tower1")
		node = tower1.head
		if node is not None:
			while node != None:
				print(node.value)
				node = node.next

		print("tower2")
		node = tower2.head
		if node is not None:
			while node != None:
				print(node.value)
				node = node.next
		else:
			print('empty')
		print("tower3")

		node = tower3.head
		if node is not None:
			while node != None:
				print(node.value)
				node = node.next
		else:
			print('empty')
		print('\n')

def move_disks(n, tower_origin, tower_destination, tower_buffer):

	'''
	Args:
	tower1, tower2, tower3 are of type TowerHannoi (curated minStack implementation)
	
	out:
	Moves the disks from tower 1 to tower 3
	'''

	# move top n-1 disks from origin to buffer, using destination as a buffer
	move_disks(n-1,tower_origin,tower_buffer,tower_destination)

	# move top from origin to destination (all other disks are in the buffer)
	move_disks(tower_origin,tower_destination)

	# move n-1 disks from buffer to destionation using origin as a buffer
	move_disks(n-1, tower_buffer, tower_destination, tower_origin)

def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    if n == 1: 
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
          
# Driver code 
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')  
# A, C, B are the name of rods 
  
# Contributed By Harshit Agrawal 




	


tower1 = TowerHannoi()
tower2 = TowerHannoi()
tower3 = TowerHannoi()

for i in [i for i in range(1,5)][::-1]:
	tower1.push(i) # initialize the first tower


tower1.display_towers(tower1, tower2, tower3)

#print(len(tower1.nodes))
#move_disks(tower1,tower2,tower3)



	# tower3.display_towers(tower1,tower2,tower3)

	# if type(tower1) != TowerHannoi: # edge case
	# 	return 0

	# if tower1.head == None and tower2.head == None:
	# 	return 'Done' # we are done. all disks moved to tower 3

	# elif tower1.head == None and (tower2.head != None and tower3.head != None):
	# 	if tower2.top()>tower3.top():
	# 		disk = tower2.pop()
	# 	else:
	# 		disk = tower3.pop()
	# 	tower1.push(disk)
	# 	move_disks(tower1,tower2,tower3)

	
	# elif tower2.head == None and tower3.head == None: # we have all disks at the start.
	# 	disk = tower1.pop()
	# 	tower2.push(disk)
	# 	move_disks(tower1,tower2,tower3)

	# elif tower2.head != None and tower3.head == None:
	# 	disk = tower1.pop()
	# 	if (tower1.head and tower2.head) and tower1.top() < tower2.top():
	# 		print(True)
	# 		tower2.push(disk)
	# 	else:
	# 		tower3.push(disk)
	# 	move_disks(tower1,tower2,tower3)

	# elif tower2.head == None and tower3.head != None:
	# 	disk = tower1.pop()
	# 	tower2.push(disk)
	# 	tower3.display_towers(tower1,tower2,tower3)
	# 	move_disks(tower1,tower2,tower3)

	# else: #tower2.nodes != None and tower3.nodes != None:
		
	# 	print('val',tower2.nodes[0].value)
		


	# 	if tower2.top() > tower3.top():
	# 		disk = tower3.pop()
	# 		print(tower3.head)
	# 		if tower3.head != None:
	# 			tower1.push(disk)
	# 		else:
	# 			tower2.push(disk)
	# 		move_disks(tower1,tower2,tower3)
	# 	else:
	# 		if tower1.top()>tower2.top() and tower1.top()<tower3.top():

	# 			disk = tower1.pop()
	# 		else:
	# 			disk = tower1.pop()
	# 		tower3.push(disk)
	# 		move_disks(tower1,tower2,tower3)