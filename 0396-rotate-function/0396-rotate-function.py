class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        n = len(nums)
        cur_val = sum([i*val for i, val in enumerate(nums)])
        max_val = cur_val
        #대충 마지막 것 뺴고 나머지 애들은 하나씩 추가됨
        # print(cur_val)
        for i in range(n):
            cur_val = cur_val + s - n*nums[n-1-i]
            max_val = max(max_val, cur_val)
        return max_val




        # values = []
        # def dps(curNums):
        #     value = 0
        #     for i in range(len(curNums)):
        #         value += i*curNums[i]
        #     values.append(value)

        # for i in range(len(nums)):
        #     dps(nums)
        #     nums.append(nums.pop(0))
        # return max(values)