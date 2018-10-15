# basic heap implementation

# Another interesting property of a complete tree is that we can 
# represent it using a single list. We do not need to use nodes and 
# references or even lists of lists. Because the tree is complete, 
# the left child of a parent (at position p) is the node that is found 
# in position 2p in the list. Similarly, the right child of the parent 
# is at position 2p+1 in the list. To find the parent of any node in the tree,
# we can simply use Python’s integer division. Given that a node is 
# at position n in the list, the parent is at position n/2. 

# Figure 2 shows a complete binary tree and also gives the list 
# representation of the tree. Note the 2p and 2p+1 relationship 
# between parent and children. The list representation of the tree, 
# along with the full structure property, allows us to efficiently traverse
#  a complete binary tree using only a few simple mathematical operations. 
#  We will see that this also leads to an efficient implementation of our 
#  binary heap.

class minHeap():

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

class maxHeap():

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def maxChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2 
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

heap = minHeap()
heap_max = maxHeap()
testlist=[7, 1,5, 11, 21, 9, 6, 3, 8, 12,13,4,10]

for i in testlist:
    heap.insert(i)
    heap_max.insert(i)

print(heap.heapList)

heap.delMin()

print(heap.heapList)

print('-'*50)

print(heap_max.heapList)

heap_max.delMax()

print(heap_max.heapList)

