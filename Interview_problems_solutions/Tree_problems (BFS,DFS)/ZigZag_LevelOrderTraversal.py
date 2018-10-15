# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
            
    def helper(self, root,total=[],height=0):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return None
        #print(root.val)
        if root.val != None:
            total.append((height,root.val))
            self.helper(root.left,total,height+1)
            self.helper(root.right,total,height+1)
        return total
    
    def zigzagLevelOrder(self, root,total=[],height=0):
        if root == None:
            return []
        ans = self.helper(root,total=[],height=0)
        
        mapping = {}
        #print(ans)
        for item in ans:
            if item[0] in mapping:
                mapping[item[0]].append(item[1])
            else:
                mapping[item[0]] = [item[1]]
        
        res = []
        zig = 1
        for key in mapping.keys():
            #print(mapping[key])
            if zig == 1:
                res.append(mapping[key])
            else:
                res.append(mapping[key][::-1])
            zig *=-1
        return res
        
        
        