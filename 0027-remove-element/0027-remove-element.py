class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for num in nums:
            if num == val:
                k+=1
        for i in range(k):
            nums.remove(val)

        return len(nums)    

