# Last updated: 6/19/2025, 11:46:33 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root, count = 0):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        '''
        - need parameter count. check if no children. if count_instance < count, return
        '''

        if root is None:
            return 0

        count += 1

        if root.left is None and root.right is None:
            return count
        
        left_tree_height = self.maxDepth(root.left, count)
        right_tree_height = self.maxDepth(root.right, count)

        return max(left_tree_height, right_tree_height)

        

        