'''
Common implementation of a Linked List.

'''

class Node():
    
    def __init__(self,value,next_pointer):
        self.value = value
        self.next = next_pointer
        
class LinkedList():
    
    def __init__(self, head):
        self.next = None #pointer to the next node
        self.head_node = Node(head,self.next) # head node and pointer
        self.nodes = [self.head_node]
        
    def __len__(self):
        return len(self.nodes)
    
    def __getitem__(self,index):
        
        if index <= self.__len__()-1 and index >= 0:
            counter = 0
            curr_node = self.head_node

            while counter != index:
                curr_node = curr_node.next #point to the next node
                counter += 1

            return curr_node.value
        
        elif self.__len__()==0:
            raise ValueError("Cannot access items of an empty list")
            
        else:
            raise ValueError("Index needs to be in range of nodes indices")
        
    def __repr__(self):

        class_name = type(self).__name__
    
        #repr can be send to eval to create the instance of that object!
        return "{}({})".format(class_name,self.head_node.value)
    
    def insert_front(self,element):
        new_node = Node(element, self.head_node)
        self.head_node = new_node
        self.nodes = [new_node] + self.nodes
        
    def insert_back(self,element):
 
        curr_node = self.head_node

        while curr_node.next is not None:
            curr_node = curr_node.next
            #print(curr_node.value)
        
        new_node = Node(element,None)
        curr_node.next = new_node
        
        self.nodes = self.nodes + [new_node]

    def remove_duplicates(self):

    	unique_dict = {}

    	curr_node = self.head_node

    	unique_ll = LinkedList(curr_node.value)

    	unique_dict[curr_node.value] = 1 # the first value is definitely unique

    	while curr_node.next != None:
    		
    		if curr_node.next.value in unique_dict:
    			curr_node.next = curr_node.next.next # re-assign pointers for duplicate values
    			#print(curr_node.next.value)
    		else:
    			unique_dict[curr_node.next.value] = 1
    			unique_ll.insert_back(curr_node.next)

    		if curr_node.next != None: # check for the last node (edge case)
    			curr_node = curr_node.next
    		
    		if curr_node.value not in unique_dict: # check the last node
    			unique_ll.insert_back(curr_node)
    			unique_dict[curr_node.value] = 1
    	
    	# if curr_node.value not in unique_dict: # check the terminal node again!
    	# 	unique_ll.insert_back(curr_node)

    	return unique_ll

L1 = LinkedList(10)
L1.insert_back(10)
L1.insert_back(5)
L1.insert_front(6)
L1.insert_back(1)

for i in range(8):
	#print('iter: ',i)
	L1.insert_back(i)

L1.insert_back(1)

for i in range(1,L1.__len__()):
	print(L1.__getitem__(i))
print('-'*50)
unique_ll = L1.remove_duplicates()

print('-'*50)
print(unique_ll.__getitem__(0))

for i in range(1,unique_ll.__len__()):
	print(unique_ll.__getitem__(i).value)


	

