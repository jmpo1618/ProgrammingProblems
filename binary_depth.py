# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, node, count):
        if node:
            return max(self.helper(node.left, count + 1), self.helper(node.right, count + 1))
        return count
            
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.helper(root, 0)
        else:
            return 0
        
    
