class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}

        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1    

        result = []
        for key, values in dic.items():
            if values > len(nums)/3:
                result.append(key)
        return result        





        