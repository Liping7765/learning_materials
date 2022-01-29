"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here

        result, _ , _ = self.dfs(root)

        return result

    def dfs(self, root):

        #key issue here is how to deal with None
        if not root:
            return None, 0, sys.maxsize

   
        left_node, left_sum, left_min = self.dfs(root.left)

        right_node, right_sum, right_min = self.dfs(root.right)

        current_total = root.val + left_sum + right_sum
        
        current_min = min(left_min, right_min, current_total)

        if current_min == left_min :
            return left_node, current_total, left_min
        if current_min == right_min:
            return right_node, current_total, right_min

        return root, current_total, current_min


"""
review
1. Biggest number of python ? 
    
"""