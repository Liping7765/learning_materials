# DFS Traversal

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        paths = []
        path =[]
        self.dfs(root, path, paths)
        return paths


    def dfs(self, root, path, paths):

        if not root:
            return 

        path.append(root.val)

        if root.left == None and root.right == None:
            paths.append("->".join([str(val) for val in path]))
            return

        self.dfs(root.left, path, paths)
        if root.left:
            path.pop()
        self.dfs(root.right, path, paths)
        if root.right:
            path.pop()

        return 

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if root is None:
            return []
            
        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()  # 回溯
        
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()


review session:
1. paths.append("->".join([str(val) for val in path]))
2. path.pop() #backtracking is necessary in this case 

"""

