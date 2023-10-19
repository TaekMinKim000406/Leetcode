class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """ 
        index = 0
        numbers= []
        while index<len(nums):
            bef_index = index
            for i in range(len(nums)-index-1):
                if nums[index+1]==nums[index]+1:
                    index+=1
                else:
                    break    
            numbers.append([bef_index, index])
            index+=1
        # print(numbers)
        result = []
        for i in range(len(numbers)):
            if numbers[i][0]==numbers[i][1]:
                result.append(str(nums[numbers[i][0]]))
            else:
                result.append(str(nums[numbers[i][0]])+'->'+str(nums[numbers[i][1]]))    

        return result