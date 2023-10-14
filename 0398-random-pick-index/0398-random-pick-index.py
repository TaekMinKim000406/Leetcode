class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)
        # self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.indices[target])
        # result = []
        # for i in range(0, len(self.nums)):
        #     if self.nums[i]==target:
        #       result.append(i)
            
        # return random.choice(result)



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)