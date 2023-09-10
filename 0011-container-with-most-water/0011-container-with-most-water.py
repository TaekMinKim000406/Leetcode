class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max_vol = 0
        # for i in range(len(height)): #0~7
        #     for j in range(len(height)-i-1): #0~6
        #         max_vol = max(min(height[i], height[i+j+1])*(j+1), max_vol)
        # return max_vol

        max_vol = 0
        start, end = 0, len(height)-1
        while start<end:
            max_vol = max(max_vol, min(height[start],height[end])*(end-start))
            if height[start]>height[end]:
                end -=1
            else:
                start += 1
        return max_vol            
