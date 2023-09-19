class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def possible(candidate):
            su = 0
            for i in range(len(candidate)):
                su += candidate[i]

            if su<target:
                for i in range(len(candidates)):
                    new_candidate = candidate[:]
                    new_candidate.append(candidates[i])
                    possible(new_candidate)
            elif su==target:
                candidate = sorted(candidate)
                if candidate not in result:
                    result.append(candidate)

        if not candidates:
            return 0

        possible([])
        


        return result



        