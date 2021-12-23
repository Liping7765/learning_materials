#BFS search 

#submission 1
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here

        if not node:
            return None

        #bfs the whole graph and clone all the nodes 

        queue = collections.deque([node])
        nodes_map = {node : UndirectedGraphNode(node.label)}


        while queue:

            curr = queue.popleft()

            for neighbor in curr.neighbors:

                if neighbor in nodes_map:
                    continue 

                queue.append(neighbor)
                nodes_map[neighbor] = UndirectedGraphNode(neighbor.label)


        #iterate the nodes_map and clone the edges 
        for original_node, cloned_node in nodes_map.items():

            cloned_node.neighbors = [ nodes_map[neighbor] for neighbor in original_node.neighbors]


        return nodes_map[node]


# to optimize the solution 
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here

        if not node:
            return None

        #bfs the whole graph and clone all the nodes 

        queue = collections.deque([node])
        nodes_map = {node : UndirectedGraphNode(node.label)}

        while queue:

            curr = queue.popleft()

            for neighbor in curr.neighbors:

                if neighbor in nodes_map:
                    nodes_map[curr].neighbors.append(nodes_map[neighbor])
                    continue 

                queue.append(neighbor)
                nodes_map[neighbor] = UndirectedGraphNode(neighbor.label)
                nodes_map[curr].neighbors.append(nodes_map[neighbor])


        return nodes_map[node]


"""

分布完成，看起来更直观
1. 找到所有点
2. 复制所有点
3. 复制所有边

但是one pass其实就能够完成三个步骤

"""
