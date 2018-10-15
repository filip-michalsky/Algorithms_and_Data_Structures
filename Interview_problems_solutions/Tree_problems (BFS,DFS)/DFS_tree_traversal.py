from time import time
from utils import BST

class DFS_Traversals(BST):

    def print_inorder(self,a=[]):


        if self.left:
            self.left.print_inorder()
        a.append(self.key)
        print(self.key)
        if self.right:
            self.right.print_inorder()
            
        return a

    def print_preorder(self,a=[]):

        if self.key:
            print(self.key)
            a.append(self.key)
        if self.left:
            self.left.print_preorder()
            
        if self.right:
            self.right.print_preorder()
            
        return a

    def print_postorder(self, a = []):

        
        if self.left:
            self.left.print_postorder()
            
        if self.right:
            self.right.print_postorder()

        if self.key:
            print(self.key)
            a.append(self.key)
        return a

BST1 = DFS_Traversals()

testlist=[7, 1,5, 11, 2, 9, 6, 3, 8, 12,13,4,10]
for i in testlist:
    BST1.insert(i)

print(BST1)

# print(BST1.print_inorder())
# print('-'*50)
print(BST1.print_preorder())
# print('-'*50)
# print(BST1.print_postorder())
