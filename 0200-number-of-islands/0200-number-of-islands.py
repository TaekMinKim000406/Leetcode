class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def visit(i,j):
            if grid[i][j]=="1":
                grid[i][j]="0"
                if i>0:
                    visit(i-1,j)
                if i<len(grid)-1:
                    visit(i+1,j)
                if j>0:
                   visit(i,j-1)
                if j<len(grid[0])-1:
                    visit(i,j+1)            

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    visit(i,j)
                    count+=1

        return count
