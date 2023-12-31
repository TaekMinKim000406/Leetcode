class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0

        nums.sort()

        max_gap = 0

        for i in range(len(nums)-1):
            max_gap = max(max_gap, nums[i+1]-nums[i])

        return max_gap    

