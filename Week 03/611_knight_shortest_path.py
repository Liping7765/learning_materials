"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortestPath(self, grid, source, destination):
        # write your code here

        if source.x == destination.x and source.y == destination.y :
            return 0

        DIRECTIONS = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, -1), (2, 1), (-2, 1), (-2, -1)]
        distance = 0
        queue = collections.deque([source])


        #copy the grid 
        visited = [ [i for i in row ] for row in grid ]

        while queue:
            
            #take out the same layer 
            for _ in range(len(queue)):

                temp = queue.popleft()

                for dx, dy in DIRECTIONS:

                    mx = temp.x + dx
                    my = temp.y + dy 

                    if self.is_valid(mx, my, grid) and not visited[mx][my]:
                        queue.append( Point(mx, my) )
                        visited[mx][my] = 1

                    if mx == destination.x and my == destination.y:
                        return distance + 1
                
            distance += 1

        return -1

    
    def is_valid(self, x, y, grid):

        return 0 <= x < len(grid) and 0 <= y < len(grid[0])




"""
review:
To read the question more carefully and avoid mistakes like this. 

"""
