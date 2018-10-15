from time import time
from utils import BST

class BST_value_getter(BST):

    def getValues(self,counter=0,depth=0,a=[]):
        
        
        if depth == 0: # return the root 
            return [self.key]

        if counter == depth: #base case
            a.append(self.key)
            return
        
        else:
            counter = counter + 1
            if self.left:
                #print("going left")
                self.left.getValues(counter,depth,a)
            else:
                b =pow(2,(depth-counter))
                
                c=["None"]
                #print(c*b)
                for i in c*b:
                    a.append(i)
            if self.right:
                self.right.getValues(counter,depth,a)
            else:
                b =pow(2,(depth-counter))
                c=["None"]
                #print(c*b)
                for i in c*b:
                    a.append(i)
        
        return a

BST1 = BST_value_getter()
testlist=[7, 0, 1,5, 11, 2, 9, 6, 0, 3, 8, 12,13,4,10]
for i in testlist:
    BST1.insert(i)

print(BST1)

print(BST1.getValues(depth=4,a=[]))