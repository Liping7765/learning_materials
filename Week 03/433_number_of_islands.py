class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here  

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 0:
                    continue 

                if visited[i][j]:
                    continue 


                count += self.find_island(i, j, grid, visited)

                
        return count 



    def find_island(self, i, j, grid, visited):

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = collections.deque([(i, j)])
        visited[i][j] = 1

        while queue:

            a, b = queue.popleft()

            for delta_x, delta_y in directions:

                x, y = a + delta_x, b + delta_y 

                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y]:

                    visited[x][y] = 1
                    queue.append((x, y))


        return 1








                



