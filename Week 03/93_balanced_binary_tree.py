"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here

        depth, result = self.check(root)

        return result 


    def check(self, root):

        if not root:
            return 0, True 

        left, is_left_balanced = self.check(root.left)
        right, is_right_balanced = self.check(root.right)


        return max(left, right) + 1, is_left_balanced and is_right_balanced and abs(left - right) <= 1

        
"""
feature of balanced tree:

1. height difference between left subtree and right subtree is not greater than 1
2. subtrees left and right are balanced as well eg. ^

note:
a. advantage of python is that it allows you return multiple values, in this case, you will be able to use
recursion to keep track of two different values 

b. for java, the work around is to create a class that stores both of the value and return the instance of such a class instead.

c. with this feature, function's argument doesn't need to be identical with return value in python.



Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

class Solution:
    
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced
        
    def validate(self, root):
        if root is None:
            return True, 0
            
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0
            
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1
"""

