class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []

        # for i in range(len(nums)):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue

        #     left = i-1
        #     right = i+1
        #     while left>=0 and right<=len(nums)-1:
        #         total = nums[left]+nums[right]+nums[i]
        #         if total == 0:
        #             result.append([nums[left],nums[right],nums[i]])
        #         elif total>0:
        #             left -=1
        #         else:
        #             right +=1   

        # return result
        for i in range(len(nums)):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 중복된 값 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

        

            #i가 중간값이라 가정



        # result = []
        # nums = sorted(nums)
        # start = 0
        # end  = len(nums)-1

        # i = 0
        # while i<len(nums):
        #     j=i+1
        #     while j<len(nums):
        #         k=j+1
        #         while k<len(nums):
        #             if nums[i]+nums[k]+nums[j] == 0:
        #                result.append([nums[i],nums[j],nums[k]])
        #             k+=1
        #         j+=1
        #     i+=1               
        # result = [x for i, x in enumerate(result) if x not in result[:i]]    

        # return result

                        


