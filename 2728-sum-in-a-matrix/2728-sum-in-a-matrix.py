class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        for row in nums:
            row.sort(reverse=True)
        # print(nums)
        new_nums = zip(*nums)
        # print(new_nums)
        result = 0
        for i in range(len(new_nums)):
            result += max(new_nums[i])

        return result