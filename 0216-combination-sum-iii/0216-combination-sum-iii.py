class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        total_nums = [1,2,3,4,5,6,7,8,9]
        result = []
        def recursive(target, k, nums):
            if k==1:
                if target not in nums and target in total_nums:
                    nums.append(target)
                    nums.sort()
                    if nums not in result:
                        result.append(nums)
            else:
                for i in range(len(total_nums)):
                    if total_nums[i] in nums:
                        continue
                    if target>total_nums[i]:    
                        recursive(target - total_nums[i], k-1, nums+[total_nums[i]])

        recursive(n,k,[])  
        return result         


        