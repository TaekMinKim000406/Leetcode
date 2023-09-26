class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #여기서 dp[1]은 ~에서 시작하는 단어가 있다는 의미 
        dp = [False] * (len(s) + 1)
        dp[0]=True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]  




        # #시간 초과
        # def findWord(start):
        #     if start == len(s):
        #         return True

        #     possible = []
        #     for i in range(len(wordDict)):
        #         if s[start:].startswith(wordDict[i]):
        #             possible.append(i)

        #     results = []
 

        #     for index in possible:
        #         results.append(findWord(start+len(wordDict[index])))

        #     if True in results:
        #         return True
        #     else:
        #         return False    

        # return findWord(0)
        