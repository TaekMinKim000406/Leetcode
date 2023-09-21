class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #동적 프로그래밍으로 해보기
        #dp[i][j]는 [i][j]까지 가는데 최소 비용
        #dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])

        for i in range(len(triangle)):
            if len(triangle[i])==1:
                continue
            else:
                for j in range(len(triangle[i])):
                    if j == 0:
                        triangle[i][j]= triangle[i-1][j] +triangle[i][j]
                    elif j == len(triangle[i])-1:
                       triangle[i][j]= triangle[i-1][j-1] +triangle[i][j]
                    else:      
                        triangle[i][j] = min(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
        return min(triangle[-1])



        #시간 초과
        # costs = []
        # def dfs(last_idx, mini_triangle, cost):
        #     if len(mini_triangle)>1:
        #         if last_idx+1 <= len(mini_triangle[1])-1:
        #             dfs(last_idx+1, mini_triangle[1:], cost+mini_triangle[1][last_idx+1])
        #         dfs(last_idx, mini_triangle[1:], cost+mini_triangle[1][last_idx])
        #     else:
        #         costs.append(cost)

        # dfs(0,triangle, triangle[0][0])

        # return min(costs)       