class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visited = []
        duplicated = []

        for num in nums:
            if num in visited:
                duplicated.append(num)
            else:
                visited.append(num)

        nums = list(set(nums))
        for num in duplicated:
            nums.remove(num)
        return nums

