# Last updated: 6/19/2025, 11:46:34 AM
class Solution(object):
    def inorderTraversal(self, root, result=None):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Initialize result list if it's None (this is for the first call)
        if result is None:
            result = []

        # Base case: if the node is None, return the result as is
        if root is None:
            return result
        
        # Traverse the left subtree
        self.inorderTraversal(root.left, result)
        
        # Append the current node's value
        result.append(root.val)
        
        # Traverse the right subtree
        self.inorderTraversal(root.right, result)
        
        return result
