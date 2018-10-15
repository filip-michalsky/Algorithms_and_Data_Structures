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
        
    
    def delete_middle_node(self,node_val = None):

        curr_node = self.head_node

        while curr_node.value != node_val:
            print(curr_node.value)
            curr_node = curr_node.next # get to the node we need to delete - skip it!
            
        while curr_node.next != None:
            curr_node.value = curr_node.next.value
            curr_node.next = curr_node.next.next
            print(curr_node.value)
            #curr_node = curr_node.next
             # move on to the next Node

            
    def insert_back(self,element):
     
            curr_node = self.head_node

            while curr_node.next is not None:
                curr_node = curr_node.next
                #print(curr_node.value)
            
            new_node = Node(element,None)
            curr_node.next = new_node
            
            self.nodes = self.nodes + [new_node]
    def insert_front(self,element):
        new_node = Node(element, self.head_node)
        self.head_node = new_node
        self.nodes = [new_node] + self.nodes
   
L1 = LinkedList(10)
L1.insert_back(9)
L1.insert_back(5)
L1.insert_front(6)
L1.insert_back(1)


for i in L1.nodes:
    print(i.value)
print('-'*30)

L1.delete_middle_node(10)

