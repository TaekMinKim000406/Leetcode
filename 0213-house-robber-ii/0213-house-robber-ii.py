class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(nums):
            now = prev = 0
            for n in nums:
                now, prev = max(now, prev + n), now
            return now
        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))



        # 시간초과
        # if len(nums)==1:
        #         return nums[0]
        # def rcv(cur, end):
        #     if cur == end:
        #         return nums[end]
        #     elif cur>end:
        #         return 0    
        #     else:
        #         return max(rcv(cur+2, end)+nums[cur], rcv(cur+1,end))

        # return max(rcv(0, len(nums)-2), rcv(1, len(nums)-1))            
        


        # 시간 초과
        # def rcv(idx, having, first):
        #     if first and idx == len(nums)-1:
        #         return 0
        #     elif idx == len(nums)-1 and having:
        #         return nums[idx]
        #     elif idx == len(nums)-1 and having == False:
        #         return 0        

        #     if having:
        #         return nums[idx]+rcv(idx+1, False, first)
        #     else:
        #         return max(rcv(idx+1, False, first), rcv(idx+1, True, first)) 
        # if len(nums)==1:
        #     return nums[0]


        # return max(rcv(0,True,True), rcv(1,False,False))