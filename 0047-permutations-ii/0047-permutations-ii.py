class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """       
        if len(nums)==0:
            return [[]]
        else:
            result = []
            for i in range(len(nums)):
                rest = nums[:i]+nums[i+1:]
                for j in self.permuteUnique(rest):
                    result.append([nums[i]]+j)

            non_duplicate = []
            for item in result:
                if item in non_duplicate:
                    continue
                else:
                    non_duplicate.append(item)    


            return non_duplicate  