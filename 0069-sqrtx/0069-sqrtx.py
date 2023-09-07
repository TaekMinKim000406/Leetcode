class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=0:
            return 0

        #탐색 시간이 길어서 탐색 범위를 줄여야 함
        # for i in range(x):
        #     if (i+1)*(i+1)==x:
        #         return i+1
        #     elif (i+1)*(i+1)>x:
        #         return i
        start = 1
        end = x

        while start<=end:
            if start**2 == x:
                return start
            if end**2==x:
                return end

            if start**2<x and x<(start+1)**2:
                return start 
            if ((end-1)**2<x and x<=end**2):
                return end-1 

            if ((start+end)//2)**2 < x:
                start = (start+end)//2
            else:
                end = (start+end)//2


