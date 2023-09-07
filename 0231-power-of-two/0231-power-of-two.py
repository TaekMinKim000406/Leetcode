class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        elif 0<n <1:
            num = n
            while(True):
                if num==1:
                    return True
                if num>1:
                    return False    
                num *=2            

        num = n
        while(True):
            if num != int(num):
                return False
            if num == 1:
                return True    
            num = num/2.0