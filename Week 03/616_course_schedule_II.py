class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here

        #set up a graph to store all edges 
        graph = [ [] for _ in range(numCourses) ]

        #degree 
        degree = [0] * numCourses 

        #create the graph and store the degree
        for node_out, node_in in prerequisites:

            graph[node_in].append(node_out)
            degree[node_out] += 1

        #BFS 

        start = [ index for index, i in enumerate(degree) if i == 0 ]
        queue = collections.deque(start)
        result = []

        while queue:

            current = queue.popleft()

            for course in graph[current]:

                

                degree[course] -= 1
                if not degree[course]:
                    queue.append(course)
            
            result.append(current)

        return result if len(result) == numCourses else []

                


                
"""
review:

1. you need to consider the situation that the graph is in a loop,
which will not provide a valid schedules

eg. a -> b -> c -> d -> b

2. how to make a graph with list comprehension ?

3. how to have index and value in the for loop ?

"""

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        
        # 建图
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1
        
        num_choose = 0
        queue = collections.deque()
        topo_order = []
        
        # 将入度为 0 的编号加入队列
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            now_pos = queue.popleft()
            topo_order.append(now_pos)
            num_choose += 1
            # 将每条邻边删去，如果入度降为 0，再加入队列
            for next_pos in graph[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
        
        if num_choose == numCourses:
            return topo_order
        return []