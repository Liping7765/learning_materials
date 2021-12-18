class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here

        count = 0
        circle = []
        for row_index in range(len(M)):

            if row_index in circle: 
                continue 

            circle += self.bfs(row_index, M)

            count += 1

        return count 

    def bfs(self, row_index, M):

        queue = collections.deque([row_index])

        result = []

        while queue:

            row = queue.popleft()
            result.append(row)

            for index, col in enumerate(M[row]):

                if col and index not in result:

                    queue.append(index)

        return result 



class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def BFS(self, student, M):
        queue = []
        queue.append(student)
        while len(queue) :
            size = len(queue)
            for i in range(0, size) :	#控制每轮搜索的点到起点的距离相同
                j = queue[0]
                del queue[0]
                M[j][j] = 2
                for k in range(0, len(M[0])):	#遍历朋友关系
                    if M[j][k] == 1 and M[k][k] == 1:	#如果M[k][k]==1，说明k没被遍历，需要继续搜索
                        queue.append(k)
    def findCircleNum(self, M):
        # Write your code here
        count = 0
        for i in range(0, len(M)):
            if M[i][i] == 1 :	#如果当前对角线为1，说明这个人位于新的联通块内
                count += 1	#计数+1
                self.BFS(i, M) #开始搜索
        return count