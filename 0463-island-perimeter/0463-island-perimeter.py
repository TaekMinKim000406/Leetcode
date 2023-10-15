class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    result +=4
                
                    if i>0 and grid[i-1][j]==1:
                        result -=1

                    if len(grid)-1>i and grid[i+1][j]==1:
                        result -=1

                    if j>0 and grid[i][j-1]==1:
                        result -=1

                    if len(grid[0])-1>j and grid[i][j+1]==1:
                        result -=1

        return result




