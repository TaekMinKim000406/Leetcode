class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dictNums = {}
        for num in nums:
            if num not in dictNums.keys():
                dictNums[num]=1
            else:
                dictNums[num]+=1
        numbers = []
        for key, value in dictNums.items():
            numbers.append([key,value])

        numbers.sort(key = lambda x: x[1], reverse=True)
        print(numbers)

        result = []
        for i in range(0,k):
            result.append(numbers[i][0])
        return result

              