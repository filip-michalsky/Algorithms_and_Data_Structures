class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        O(n) time - each node visit only once
        O(n) space -dictionary stores the entire tree
        NOTE: it is possible to construct O(1) space if we keep track of the last elem visited in a level. If
        level changes, we know we are at the last element (the right most one)
        """

        dict_list = self.get_list_depths(node=root,dict_levels = {},level = 0)
        result = []
        for level in sorted(dict_list):
            result.append(max(dict_list[level]))

        return result

    def get_list_depths(self,node,dict_levels = {},level = 0):

        if node.val == None:
            return
        if level not in dict_levels:
            dict_levels[level] = [node.val]
        else:
            dict_levels[level].append(node.val)

        if node.left:
            self.get_list_depths(node=node.left,dict_levels=dict_levels,level = level+1)
        if node.right:
            self.get_list_depths(node=node.right,dict_levels=dict_levels,level=level+1)
        return get_list_depths