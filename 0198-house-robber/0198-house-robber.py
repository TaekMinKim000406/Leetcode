class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        # dp 배열 초기화
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # dp를 이용한 최대 가치 계산
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
        # #i번째를 훔치면 i+2 or i+3 2가지 케이스가 있음


        # def choose(cost, i):
        #     cost = cost + nums[i]
        #     ch1= cost
        #     ch2= cost 
            
        #     if i + 2 < len(nums):
        #         ch1 = choose(cost, i + 2)
        #     if i + 3 < len(nums):
        #         ch2 = choose(cost, i + 3)
        #     return max(ch1, ch2)

        # if len(nums)==1:
        #     return nums[0]


        # return max(choose(0, 0), choose(0, 1))