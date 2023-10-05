class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])

        if not matrix:
            return 0
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])  # 문자열을 정수로 변환
                if i > 0 and j > 0 and dp[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

        return max_side * max_side

        # #시간 초과
        # matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]

        # for i in range(1, min(m,n)):
        #     for j in range(0, m-1):
        #         for k in range(0, n-1):
        #             if matrix[j][k] >=1:
        #                 matrix[j][k] = min(matrix[j+1][k], matrix[j][k+1] ,matrix[j+1][k+1])+1
        
        
        # return (max(max(row) for row in matrix))**2


