class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = range(1,n+1)
        combinations = []
        def combinate(start_index , last, index):
            if last == 0:
                combinations.append(index)
                return

            if last == len(nums) - start_index:
                combinations.append(index + nums[start_index:])
            elif last> len(nums) - start_index:  
                return
            else:
                combinate(start_index + 1 , last, index[:])
                combinate(start_index + 1 , last-1, index+[nums[start_index]])

        combinate(0,k,[])
        return combinations    



