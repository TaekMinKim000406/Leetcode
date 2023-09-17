class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
    
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 첫 번째 행 초기화: word1을 빈 문자열로 변환하는 경우
        for i in range(m + 1):
            dp[i][0] = i
        
        # 첫 번째 열 초기화: 빈 문자열을 word2로 변환하는 경우
        for j in range(n + 1):
            dp[0][j] = j
        
        # 나머지 부분 채우기
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 현재 문자가 같으면 아무 작업도 필요하지 않습니다.
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 현재 문자가 다르면 세 가지 작업 중 가장 작은 작업 수를 선택합니다.
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        

                    # dp[i-1][j]: 문자를 삭제하는 작업
                    # dp[i][j-1]: 문자를 삽입하는 작업
                    # dp[i-1][j-1]: 문자를 교체하는 작업
        # 마지막 칸에는 최소 작업 수가 저장되어 있습니다.
        return dp[m][n]

        