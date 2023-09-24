class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        total = []
        for i in range(len(nums)-2):
            flag = False
            j,k=i+1,len(nums)-1
            while (j<k):
                cur = nums[i]+nums[j]+nums[k]
                total.append(cur)
                if cur>target:
                    k-=1
                elif cur<target:
                    j+=1
                else:
                    flag= True
                    break
            if flag:
                break
        result = total[0]
        for i in range(1, len(total)):                        
            if abs(target - total[i]) < abs(result-target):
                result = total[i]
        return result        




        