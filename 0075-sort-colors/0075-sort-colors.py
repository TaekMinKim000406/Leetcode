class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num0=0
        num2=0
        for i in range(len(nums)):
            if nums[i]==0:
                num0+=1
            elif nums[i]==2:
                num2+=1

        for i in range(num0):
            for j in range(len(nums)-1, -1 , -1):
                if nums[j] == 0:
                    nums.pop(j)
                    break
            nums.insert(0,0)
        

        for i in range(num2):
            nums.remove(2)
            nums.append(2)

        
