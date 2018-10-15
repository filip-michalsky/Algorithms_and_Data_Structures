from time import time
from utils import BST, LL, Node
import gc
'''
Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth (e.g., if you have a tree with depth D, you will have D linked lists)
'''

class BST_value_getter(BST):
    

    def getValues(self,counter=0,depth=0,a=[]):
    # this O(n * D) where D is depth and n is num elems is inefficient! There is a more efficient solution!
        # Filip's old solution.
        if depth == 0: # return the root, covers the edge case of an empty BST
            return [self.key] if self.key else a 
        if counter == depth: #base case we arrive to the leaf
            a.append(self.key)
            return
        else:
            counter += 1 # increment depth counter
            if self.left:
                #print('going left')
                self.left.getValues(counter,depth,a) # recurse left
            if self.right:
                #print('going right')
                self.right.getValues(counter,depth,a) # recurse right
        return a
    
    def createLevelLinkedList(self,lists=LL(),level=0):
        # this only requires traversal of each node once!
        # adaptation of pre-order traversal DFS with recording leves
        # runtime is O(n) and space complexity is O(n) as well.

        if self.key == None: # base case
            return

        if lists.__len__() == level: # level not contained in the Linked list of linked lists
            '''
            Since levels are always traversed in order, if this is the first time we reached
            some level, we must have seen levels from 0 to level - 1, adn thus we can safely add
            this level to the end.
            '''
            curr_list = LL()
            lists.insert(curr_list)
        else:
            curr_list = lists.__getitem__(level) # return a linked list at position indicated by level
        
        curr_list.insert(self.key) # insert ket in linked list for current depth
        if self.left:
            self.left.createLevelLinkedList(lists = lists,level=level+1)
        if self.right:
            self.right.createLevelLinkedList(lists = lists,level=level+1)

        return lists


BST1 = BST_value_getter()
testlist=[7, 0, 1,5, 11, 2, 9, 6, 0, 3, 8, 12,13,4,10,45]
for i in testlist:
    BST1.insert(i)
print(BST1)

lists = BST1.createLevelLinkedList(level=0)

for ll in range(len(lists)): 
    curr_ll = lists.__getitem__(ll) # access current linked list at a position ll
    print('Printing nodes at level: ',ll)
    for j in range(len(curr_ll)): # access all elements in the current linked list
        print(curr_ll.__getitem__(j))

# def main():
# ##Filip's own older solution without the book

#     # create a test BST
#     BST1 = BST_value_getter()
#     testlist=[7, 0, 1,5, 11, 2, 9, 6, 0, 3, 8, 12,13,4,10,45]
#     for i in testlist:
#         BST1.insert(i)
#     print(BST1)
#     ########
#     # Algorithms solution.
#     depth = 0
#     NEXT_LEVEL = True
#     result = []
#     running_len = 0

#     while NEXT_LEVEL:
#         # create a linked list for each level and append to result
#         a = BST1.getValues(depth=depth,a = [])
        
#         if len(a)<1:
#             NEXT_LEVEL = False
#             print("done")
#             break

#         new_ll = LL()
#         #print('elems at depth',depth)
#         for elem in a:
#             new_ll.insert(elem)
#         result.append(new_ll)
#         depth+=1

#     return result

# if __name__ == '__main__':
#     all_lists = main()
#     print(len(all_lists))
#     for i in range(len(all_lists)):
#         print('Printing a linked list values at depth',i)
#         for j in range(len(all_lists[i].nodes)):
#             print(all_lists[i].nodes[j].val)
#         print('-'*30)