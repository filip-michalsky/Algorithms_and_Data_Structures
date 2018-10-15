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

    def kth_to_last(self,index=None):

        # get to the k-th item
        if index <= self.__len__()-1 and index >= 0:
            counter = 0
            curr_node = self.head_node

            while counter != index:
                curr_node = curr_node.next #point to the next node
                counter += 1
        
        elif self.__len__()==0:
            raise ValueError("Cannot access items of an empty list!")
        else:
            raise ValueError("Index needs to be in range of nodes indices!")

        list_of_nodes = []
        while curr_node != None:
            list_of_nodes.append(curr_node.value)
            curr_node = curr_node.next
        
        return list_of_nodes
    		
L1 = LinkedList(10)
L1.insert_back(10)
L1.insert_back(5)
L1.insert_front(6)
L1.insert_back(1)

# for node in L1.nodes:
#     print(node.value)

nodes = L1.kth_to_last(index=1)

print(nodes)



	

