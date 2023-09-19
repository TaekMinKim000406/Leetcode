class Solution(object):
    def combinationSum2(self, candidates, target):
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret
    
    def dfs(self, nums, target, idx, path, ret):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)
    # def combinationSum2(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
        # # 시간 초과
        # if not candidates:
        #     return 0

        # new_candidates = sorted(candidates)
        # for i in range(len(new_candidates)):
        #     if  new_candidates[i]>target:
        #         new_candidates = new_candidates[:i]
        #         break

        # result = []

        # def find(nums, remain): #nums는 index를 저장한 배열
        #     if remain == 0:
        #         way = [new_candidates[nums[i]] for i in range(len(nums))]
        #         if not way in result:
        #             result.append(way) 
        #     elif remain>0:
        #         for i in range(nums[-1]+1, len(new_candidates)):
        #                 new_nums = nums +[i]
        #                 new_remain = remain - new_candidates[i]
        #                 find(new_nums, new_remain)

        # for i in range(len(new_candidates)):
        #     if new_candidates[i]<target:
        #         find([i], target - new_candidates[i])
        #     elif new_candidates[i]==target:
        #         if not [new_candidates[i]] in result:
        #             result.append([new_candidates[i]])
        #     else:
        #         break    

        # return result
