
'''
Given a sorted, increasing-order array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

'''

class myBST():

    def __init__(self,key = None, parent = None):
        # quick BST structure
        self.key = key
        self.parent = parent
        self.right = None
        self.left = None

    def insert(self,key):
        # insertion to a tree
        if self.key == None: # edge case: key of node is None
            self.key = key
            
        else:
            node = self

            if key > node.key: 
                if node.right: # if there is a right child, recurse right, else create new node
                    node.right.insert(key)
                else:
                    self.right = self.__class__(key,node)
                    self.right.key = key

            else: 
                if node.left:
                    node.left.insert(key)
                else:
                    self.left = self.__class__(key,node)
                    self.left.key = key

    def __str__(self):
        "Returns ASCII drawing of the tree"
        s = str(self.key)
        if (self.left is not None) or (self.right is not None):
            ws = len(s)
            sl, wl, cl = [''], 0, 0
            if self.left is not None:
                sl = str(self.left).splitlines()
                wl = len(sl[0])
                cl = len(sl[0].lstrip(' _'))
            sr, wr, cr = [''], 0, 0
            if self.right is not None:
                sr = str(self.right).splitlines()
                wr = len(sr[0])
                cr = len(sr[0].rstrip(' _'))
            while len(sl) < len(sr):
                sl.append(' ' * wl) 
            while len(sr) < len(sl):
                sr.append(' ' * wr)
            s = s.rjust(ws + cl, '_').ljust(ws + cl + cr, '_')
            s = [s.rjust(ws + wl + cr).ljust(ws + wl + wr)]
            s = '\n'.join(s + [l + (' ' * ws) + r for (l,r) in zip(sl, sr)])
        return s
    
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

        

bst = myBST()

a = range(31)

bst.create_minimal_tree(a)

print(bst)
