class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num not in list(dic.keys()):
                dic[num]=1
            else:
                dic[num]+=1    

        values = list(dic.values())
        values.sort(reverse=True)
        for key,val in dic.items():
            if val == values[0]:
                return key