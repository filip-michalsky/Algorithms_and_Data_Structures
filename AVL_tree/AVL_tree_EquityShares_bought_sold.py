#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:43:20 2017

@author: filipmichalsky

Transaction Log: Barren Wuffett owns a small investment firm that
trades a single volatile mutual fund. Hundreds of times a second, brokers buy and sell shares of
the fund at different prices as the price dramatically fluctuates throughout the day. At any given
time, Barren wants to know how many transactions were traded that day within a given price range.
Help Barren design his transaction log; maybe he will share his profits with you! The transaction
log must support three operations:
    
• add transaction: adds a single transaction into the log containing the the number of
shares traded at a given price. A negative price means a broker sold shares, and a zero or
positive price means shares were purchased.

• sold in range: for a given inclusive price range, return the total number of shares that
brokers sold at a price within the given range.

• bought in range: for a given inclusive price range, return the total number of shares
that brokers bought at a price within the given range.

You want to support all of these operations in O(log n) time for a transaction log containing n
transactions, so you decide to use a single modified AVL tree to store all the transaction information.
Code implementing an AVL tree is provided in the problem set template. When describing
algorithms, you may describe in terms of any of the BST or AVL operations discussed in class.

"""

from AVL import AVL

class Transaction():
    def __init__(self, shares, price):
        self.shares = shares
        self.price = abs(price)
        
        if price >= 0:
            self.type = "bought"
            self.bought = shares
            self.sold = 0
        else:
            self.type = "sold"
            self.sold = shares
            self.bought = 0
        
        self.min = abs(price) #want to track the max price left and also right
        self.max = abs(price)
        
        #############################################
        # Part (a): Add any additional storage here #
        #############################################
    
    def __lt__(self, other):
        "Evaluate comparison between two transactions: (self < other)"
        ##########################
        return abs(self.price) < abs(other.price) #maybe add abs value depending on your structure??
        ##########################
        #return True         # return a boolean

    def __str__(self):
        return str(self.shares) + '@' + str(self.price)

class TransactionLog(AVL):
    def add_transaction(self, shares, price):
        "Adds a transaction to the transaction log"
        node = super().insert(Transaction(shares, price))

    def update(self):
        "Augments AVL update() to fix any properties calculated from children"
        super().update()
        #################################################
        #calculate min and max in subtree
        
        if not self.right and not self.left and self.parent:
            self.parent.key.min = min(self.key.min,self.parent.key.min)
            self.key.min = self.key.price
        
            self.parent.key.max = max(self.key.max,self.parent.key.max)
            self.key.max = self.key.price
        
        if self.right and self.left:
            self.key.min = min(self.right.key.min,self.left.key.min,self.key.price)
            self.key.max = max(self.right.key.max,self.left.key.max,self.key.price)
        
        elif self.parent:
            if self.parent.left == self:
                if self.right:
                    self.key.max = max(self.key.price, self.right.key.max)
                else:
                    self.key.max = self.key.price
                    
            if self.parent.right == self:
                if self.left:
                    self.key.min = min(self.key.price,self.left.key.min)
                else:
                    self.key.min = self.key.price
                
        #calculate shares bought and sold in the subtree      
        if self.key.type == "bought":
            self.key.bought = self.key.shares
            self.key.sold = 0
        else:
            self.key.sold = self.key.shares
            self.key.bought = 0
            
        if self.right:
            self.key.bought += self.right.key.bought
            self.key.sold += self.right.key.sold
            
        if self.left:
            self.key.bought += self.left.key.bought
            self.key.sold += self.left.key.sold
            
        # Part (a): Add any additional maintenence here #
        #################################################

    def sold_in_range(self, range_min, range_max):
        "Returns the number of shares sold within an inclusive price range"
        if self.key is None:
            return 0
        count = 0
        #print(self)
        ##########################
        #print(self.key.max)
        #print(self.key.price)
        #print(self.key.min)
        #if out of range, return 0
        
        if self.key.max < range_min or self.key.min > range_max:
            return 0

        #when min and max completely in range - add the subtree
        elif self.key.min >= range_min and self.key.max <= range_max:
            count += self.key.sold
        
        elif self.key.sold == 0:
            return 0

        else:
            #if partially in range, and the price itself is in range, return it
            if range_min <= self.key.price <= range_max:
                if self.key.type == "sold":
                    count += self.key.shares
                    
                if self.right:
                    count += self.right.sold_in_range(range_min,range_max)
                
                if self.left:
                    count += self.left.sold_in_range(range_min,range_max)
            
            elif self.key.price > range_max:
                
                if self.left:
                    count += self.left.sold_in_range(range_min,range_max)
                    
            elif self.key.price < range_min:
                if self.right:
                    count += self.right.sold_in_range(range_min,range_max)
                    
        
        return count
        
    
    def bought_in_range(self, range_min, range_max):
        "Returns the number of shares bought within an inclusive price range"
        if self.key is None:
            return 0
        count = 0
        ##########################

        #if out of range, return 0
        if self.key.max < range_min or self.key.min > range_max:
            return 0
        
        elif self.key.bought == 0:
            return 0
        #when min and max completely in range
        elif self.key.min >= range_min and self.key.max <= range_max:
            count += self.key.bought

        else:
            #if partially in range, and the price itself is in range, return it
            if range_min <= self.key.price <= range_max:
                if self.key.type == "bought":
                    count += self.key.shares
            
                if self.right:
                    count += self.right.bought_in_range(range_min,range_max)
                    
                if self.left:
                    count += self.left.bought_in_range(range_min,range_max)
                    
            elif self.key.price > range_max:
                
                if self.left:
                    count += self.left.bought_in_range(range_min,range_max)
                    
            elif self.key.price < range_min:
                
                if self.right:
                    count += self.right.bought_in_range(range_min,range_max)
            

        
        ##########################
        return count


##################
# Test your code #
##################
def parse_input(s):
    ops = s.split('\n')
    for i in range(len(ops)):
        ops[i] = ops[i].split(' ')
        for j in range(1, len(ops[i])):
            ops[i][j] = int(ops[i][j])
    return ops

def out_from_in(ops):
    # outputs return values from range queries on separate lines
    t = TransactionLog()
    outs = []
    for i, op in enumerate(ops):
        if op[0] == 'add':
            t.add_transaction(op[1], op[2])
        if op[0] == 'bought':
            n = t.bought_in_range(op[1], op[2])
            outs.append(str(n))
        if op[0] == 'sold':
            n = t.sold_in_range(op[1], op[2])
            outs.append(str(n))
    return ' '.join(outs)

def test_on_case(case):
    with open('cases/' + str(case) + '.in', 'r') as f:
        s = f.read()
        out = out_from_in(parse_input(s))
    with open('cases/' + str(case) + '.out', 'r') as f:
        golden = f.read()
        print(golden)
        print(out)
        if out == golden:
            print('Passed test case ' + str(case) + '!')
        else:
            print('Failed test case ' + str(case) + '... :(')

if __name__ == '__main__':
    for i in [1, 2]:
        test_on_case(i)