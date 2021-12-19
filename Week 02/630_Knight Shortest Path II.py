#BFS
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here

        if not grid: 
            return -1
        
        step = 0
        grid[0][0] = 1
        queue = collections.deque([[0,0]])

        while queue:

            step += 1

            for _ in range(len(queue)):

                x, y = queue.popleft()

                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return grid[x][y]

                self.add_step(x, y, queue, step, grid)

        
        return -1 


    def add_step(self, x, y, queue, step, grid):

        directions = [[1, 2], [-1, 2], [2, 1], [-2, 1]]

        for delta_x, delta_y in directions:
            row = delta_x + x
            col = delta_y + y

            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
                continue 

            if grid[row][col] != 0:
                continue
            
            grid[row][col] = step
            queue.append([row, col]) 


            









