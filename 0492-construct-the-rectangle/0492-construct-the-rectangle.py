class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        nums = []
        for i in range(1, int(area**0.5)+1):
                if area%i==0:
                    nums.append([area//i, i])


        return nums[-1]