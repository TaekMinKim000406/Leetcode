class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]



        # #시간 초과
        # m = len(grid[0])-1
        # n = len(grid)-1

        # costs = []
        # def findpath(remain_m, remain_n, cost):
        #     if remain_m>0:
        #         findpath(remain_m-1, remain_n, cost+grid[len(grid)-1-remain_n][len(grid[0])-remain_m])
        #     if remain_n>0:
        #         findpath(remain_m, remain_n-1, cost+grid[len(grid)-remain_n][len(grid[0])-1-remain_m])
        #     if remain_m==0 and remain_n == 0:
        #         costs.append(cost)

        # findpath(m,n,grid[0][0])

        # return min(costs)        


