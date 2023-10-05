class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0 
        while i<len(nums)-2:
            if nums[i]==nums[i+1]==nums[i+2]:
                i+=3
            else:
                return nums[i]
        return nums[i]            



        