from time import time
from utils import BST
import gc
'''
Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth (e.g., if you have a tree with depth D, you will have D linked lists)
'''
class BST_with_height(BST):

    def __init__(self, key = None, parent = None):
        "Initializes a BST node"
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def create_minimal_tree(self,arr):
        # takes sorted increasing array of unique elements and creates a minimal height tree.
        mid = len(arr)//2
        self.insert(arr[mid]) # insert middle element

        left = [i for i in arr[:mid]]
        right = [i for i in arr[mid+1:]]

        #print(left,right)
        if left: # recurse on the left half of array
            self.create_minimal_tree(left)
        if right: # recurse on the right half of the array
            self.create_minimal_tree(right)

    def getHeight(self):

        if self.key == None:
            return -1

        if (not self.right) and (not self.left): # leaf, return
            return -1
        elif not self.right: # right child does not exist
            return self.left.getHeight() + 1
        elif not self.left: # left child does not exist
            return self.right.getHeight() + 1

        else: # both children exist, return max height of subtree + 1
            return max(self.left.getHeight(),self.right.getHeight())+1
    

    def checkBalanced(self):
        # not the most efficient solution -> O ( N log N)
        if self.key == None: # base case
            return True

        if self.left and self.right: # both children exist, can recurse
            heightDiff = abs(self.left.getHeight()-self.right.getHeight())
        elif self.left: # only left child exists
            heightDiff = self.left.getHeight()
        elif self.right: # only right child exists
            heightDiff = self.right.getHeight()
        else: # leaf node
            return -1

        if heightDiff > 1:
            return False

        else:
            if self.left:
                self.left.checkBalanced()
            if self.right:
                self.right.checkBalanced()

        return True


BST1 = BST_with_height()
testlist=range(20)#[-1, 7, 0, 1,5, 11, 2, 9, 6, 0, 3, 8, 12,13,4,10,45]#
BST1.create_minimal_tree(testlist)
    
print(BST1)
print(BST1.checkBalanced())