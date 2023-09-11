class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # #시간 초과로 폐기
        # sums = []
        # for i in range(len(nums)):      
        #     sums.append(sum(nums[:i+1]))

        # #sums[j] - sums[i]가 최대가 되는 것을 찾으면 됨(j>i)
        # start = 0
        # end = len(nums)-1
        # #단일에서 우선 최고인 것을 최대라 가정
        # max_sum = max(nums + sums)

        # for i in range(len(nums)-1):
        #     if i == 0:
        #         continue
        #     si = min(sums[0:i])
        #     sj = max(sums[i:])
        #     max_sum = max(max_sum, sj-si)
        # return max_sum    
        
        #기본 베이스 생각: i번째 이전 값들이 포함될지 아닐지는 i번째와 i번째 까지의 합 중의 최대 값을 통해 결정하면 된다.
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            #CurSum은 i번째를 포함하고 i번쨰 원소까지의 최대 집합
            #쉽게 생각해서 i-1번 전까지 집합의 합을 i번쨱로 확장시킬 떄 이를 더하는게 유리한지 아닌지를 검사.
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum     
