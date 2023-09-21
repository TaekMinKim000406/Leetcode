class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = []

        for attempt in range(0, 2**n):
            value = attempt
            lis = []
            exp = n - 1

            while exp >= 0:
                if value >= 2**exp:
                    lis.append(exp)
                    value -= 2**exp
                exp -= 1
            
            result.append(lis)

        res = []
        for i in range(len(result)):
            res.append([nums[x] for x in result[i]])
        return res

        
            

