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

    def insert_back(self,element):
     
            curr_node = self.head_node

            while curr_node.next is not None:
                curr_node = curr_node.next
                #print(curr_node.value)
            
            new_node = Node(element,None)
            curr_node.next = new_node
            
            self.nodes = self.nodes + [new_node]
    
    def removeNthFromEnd(self, n):
        
        curr_node = self.head_node

        len_list = len(self.nodes)

        cnt = 0
        #print(len_list)

        print(curr_node.next.value)

        while cnt - 1 != n:
             
             curr_node.next = curr_node
             print(curr_node.value)
             cnt+=1

        node = curr_node
        print('cnt:',cnt)
        print(node.value,node.next.value)
        if node.next:
            node.next = node.next.next
        else:
            node.next = None




L1 = LinkedList(1)
L1.insert_back(2)
L1.insert_back(3)
L1.insert_back(4)
L1.insert_back(5)
L1.insert_back(6)

print([i.value for i in L1.nodes])


L1.removeNthFromEnd(4)

print([i.value for i in L1.nodes])