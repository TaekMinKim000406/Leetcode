class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        result = float(dividend) / float(divisor)
        if dividend * divisor<0 and not (result == int(result)):
            result = dividend // divisor + 1
        else:    
            result = dividend // divisor
        
        if result> 2**31 -1:
            return 2**31 -1
        elif result< -2**31:
            return -2**31
        else:
            return result
