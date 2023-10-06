class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def sorting(num1,num2):
            if int(num1+num2)>int(num2+num1):
                return True
            else:
                False    

        # nums.sort(reverse = True,key=lambda x: str(x))
        nums = [str(x) for x in nums]
        # nums.sort(reverse=True)

        for j in range(len(nums)-1):
            for i in range(len(nums)-1-j):
                if not sorting(nums[i], nums[i+1]):
                    nums[i],nums[i+1] = nums[i+1],nums[i]


        print(nums)
        result = ''
        for num in nums:
            result+=str(num)
        return str(int(result))
        


