#BFS

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here

        if not root:
            return [] 

        queue = collections.deque([root])

        result = []
        while queue:

            result.append([ node.val for node in queue ])

            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

        return result

                

"""
review session:

1. queue = collections.deque([root])
    queue.popleft() -> first 
    queue.pop()  -> last 
    queue.append() ->
    queue.appendleft() ->

2. [node.val for node in queue]

3. while queue: 

4. len(queue)


"""


#可以尝试双队列 和 dummy node
