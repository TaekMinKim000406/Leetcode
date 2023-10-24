from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def fact(n):
            if n <= 1:
                return 1
            else:
                return n*fact(n-1)    
        my_counter = Counter(nums)

        result = 0
        for key, value in my_counter.items():
            if value>1:
                result += (fact(value)/fact(value-2)/fact(2))
        return result        


        