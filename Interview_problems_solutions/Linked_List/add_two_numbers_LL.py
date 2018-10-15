# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # only beat 14% of submissions!

        # loop through each ll and get the vals     
        l1_vals,l2_vals = [],[]
        
        while l1:
            l1_vals.append(str(l1.val))
            l1 = l1.next
            
        while l2:
            l2_vals.append(str(l2.val))
            l2 = l2.next
            
        # join strings, reverse, change type to int and add up to total
        l1_vals, l2_vals = "".join(l1_vals),"".join(l2_vals)
        l1_vals, l2_vals = int(l1_vals[::-1]),int(l2_vals[::-1])
        total = l1_vals + l2_vals
        
        # change total to str, reverse and split
        total_vals = str(total)[::-1]
        
        total_vals = [i for i in total_vals]
        
        # create new ll, and insert new vals
        new_ll = ListNode(total_vals.pop(0))
        node = new_ll
        while total_vals:
            val = total_vals.pop(0)
            if node.next:
                node = node.next
            new_node = ListNode(val)
            node.next = new_node
        return new_ll

