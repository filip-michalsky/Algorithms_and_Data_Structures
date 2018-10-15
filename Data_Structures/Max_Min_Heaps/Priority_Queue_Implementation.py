#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:34:51 2017

@author: filipmichalsky

 Priority Queue is a data structure supporting three operations:
     
• INSERT inserts an integer into the queue in O(log n) time,
• BEST returns a copy of the best integer in O(1) time, and
• EXTRACTBEST removes the best integer in O(log n) time,

where n is the number of integers in the data structure at the time of the operation. Different
Priority Queues have different definitions of best. For example, a Min Priority Queue is a Priority
Queue where best means the minimum integer contained in the Queue.

______________________________
Implementation of Priority Queue. Both max and min-heaps

as well as r-th heap (composed of [max heap , min heap] with max elem smaller 
than min element in min heap).
-------------------------------

"""
from math import ceil

class MinPriorityQueue:
    def __init__(self):     # initialize
        self.A = []         # list where heap is stored

    def best(self):         # returns best, without modifying heap
        if len(self.A) < 1:
            return None     # return None if queue empty
        return self.A[0]

    def insert(self, v):    # inserts v, maintaining heap
        self.A.append(v)
        node = len(self.A) - 1
        parent = (node - 1) // 2 
        while (0 <= parent) and (self.A[node] < self.A[parent]):
            self.A[parent], self.A[node] = self.A[node], self.A[parent]
            node = parent
            parent = (node - 1) // 2

    def extract_best(self): # removes best, maintaining heap
        if len(self.A) < 1:
            return None     # return None if queue empty
        node = 0
        out = self.A[node]
        self.A[node] = self.A[-1]
        self.A.pop()
        while True:
            left  = 2 * node + 1
            right = 2 * node + 2
            best = node
            if right < len(self.A) and self.A[right] < self.A[best]:
                best = right
            if left  < len(self.A) and self.A[left]  < self.A[best]:
                best = left
            if node != best:
                self.A[best], self.A[node] = self.A[node], self.A[best]
                node = best
            else:
                return out

class MaxPriorityQueue:
    def __init__(self):     # initialize
        self.A = []         # list where heap is stored

    def best(self):         # returns best, without modifying heap
        if len(self.A) < 1:
            return None     # return None if queue empty
        return self.A[0]

    def insert(self, v):    # inserts v, maintaining heap
        self.A.append(v)
        node = len(self.A) - 1
        parent = (node - 1) // 2 
        while (0 <= parent) and (self.A[node] > self.A[parent]):
            self.A[parent], self.A[node] = self.A[node], self.A[parent]
            node = parent
            parent = (node - 1) // 2

    def extract_best(self): # removes best, maintaining heap
        if len(self.A) < 1:
            return None     # return None if queue empty
        node = 0
        out = self.A[node]
        self.A[node] = self.A[-1]
        self.A.pop()
        while True:
            left  = 2 * node + 1
            right = 2 * node + 2
            best = node
            if right < len(self.A) and self.A[right] > self.A[best]:
                best = right
            if left  < len(self.A) and self.A[left]  > self.A[best]:
                best = left
            if node != best:
                self.A[best], self.A[node] = self.A[node], self.A[best]
                node = best
            else:
                return out

class RPriorityQueue:
    def __init__(self, r):  # Implement me
        self.r = r          # r should not change after initialization
        self.n = 0           # length of the array
        self.Max=MaxPriorityQueue()
        self.Min=MinPriorityQueue()
                #assume our median starts as 0
        #done!!!
        #self.Min.insert()    #calls the function from this class
        
    def best(self):         # Implement me
        if self.n<1:
            return None
        return self.Max.best()   #This will be the rth number in 
    
    def insert(self, v):    # Implement me
        if self.n==0:
            self.Max.insert(v)
        self.n+=1
        
        if v > self.Max.best():
            self.Min.insert(v)

        if len(self.Min.A) > (self.n-(ceil(self.r*self.n))):
            self.Max.insert(self.Min.extract_best())  #extract min of min heap and insert to max heap
        
        #check the greater than or greater than or equal to for the lengths!
        
        if v < self.Max.best():
            self.Max.insert(v)

        if len(self.Max.A) > ceil(self.r*self.n):
            self.Min.insert(self.Max.extract_best()) #extract max of max heap and insert to min heap
        
        #len(self.Min.A)>self.r*self.n #how to access the length and comparison
        #ceil()
        #
    def extract_best(self): # Implement me
        if self.n<1:
            return None
        out=self.Max.extract_best() #extracts the rnth element
        self.n-=1
        if len(self.Max.A) < ceil(self.r*self.n):
            self.Max.insert(self.Min.extract_best())
        
        return out

##################
# Test your code #
##################
def parse_input(s):
    ops = s.split('\n')[:-1]
    for i in range(len(ops)):
        ops[i] = ops[i].split(' ')
        if 1 < len(ops[i]):
            ops[i] = [ops[i][0], int(ops[i][1])]
    return ops

def out_from_in(kind, ops):
    # outputs return values from best() and extract_best() on separate lines
    if kind == 'min':
        q = MinPriorityQueue()
    elif kind == 'max':
        q = MaxPriorityQueue()
    elif kind[0] == 'r':
        r = float(kind[1:])
        q = RPriorityQueue(r)
    else:    
        print('kind not recognized... :(')
        return ''
    s = ''
    for op in ops:
        if op[0] == 'insert':
            q.insert(op[1])
        if op[0] == 'best':
            best = q.best()
            s += str(best) + ' '
        if op[0] == 'extract_best':
            best = q.extract_best()
            s += str(best) + ' '
    return s

def test_queue_on_case(kind, case):
    with open('cases/' + str(case) + '.in', 'r') as f:
        s = out_from_in(kind, parse_input(f.read()))
    with open('cases/' + str(case) + kind + '.out', 'r') as f:
        if s == f.read():
            print(f'{kind} queue passed test case {case}!')
        else:
            print(f'{kind} queue failed test case {case}... :(')

if __name__ == '__main__':
    for case in [1, 2]:
        for kind in ['min', 'max', 'r0.5', 'r0.4', 'r0.8']:
            test_queue_on_case(kind, case)


