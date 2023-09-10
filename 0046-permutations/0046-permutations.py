class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        permutations = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i + 1:]
            for perm in self.permute(rest):
                permutations.append([nums[i]] + perm)

        return permutations


        