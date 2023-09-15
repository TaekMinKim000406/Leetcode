class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value = nums[0]
        index = 0

        for i in range(len(nums)):
            min_value = min(min_value, nums[i])
            index = i

        return min_value 
