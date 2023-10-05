class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return len(nums)
        nums.sort()
        count = 0
        i = 0
        while i < len(nums)-count - 2:
            if nums[i]==nums[i+1] ==nums[i+2]:
                nums.pop(i)
                nums.append('_')
                count +=1
            else:
                i+=1    

        return len(nums)-count
                




