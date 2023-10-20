class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
      
        second_num = -999999999
        stck = []
        # Try to find nums[i] < second_num < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_num:
                return True
            # always ensure stack can be popped in increasing order
            while stck and stck[-1] < nums[i]:
				second_num = stck.pop()  # this will ensure  second_num < stck[-1] for next iteration

            stck.append(nums[i])
        return False
        # not_valid = None
        # for i in range(len(nums)-2):
        #     if not_valid and nums[i]>=not_valid:
        #         continue
        #     numbers = []
        #     for j in range(i+1, len(nums)):
        #         if nums[j]>nums[i]:
        #             numbers.append(nums[j])

        #     if numbers !=sorted(numbers):
        #         return True
        #     else:
        #         if not_valid is None:
        #             not_valid = nums[i]
        #         else:
        #             not_valid = min(not_valid, nums[i])  


        # return False        




