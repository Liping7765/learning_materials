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