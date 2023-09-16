class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)

        if len(result)==0:
            return [-1,-1]
        else:
            return [result[0], result[-1]]    


        