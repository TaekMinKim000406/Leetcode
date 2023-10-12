class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            num = str(num)
            result = 0
            for digit in num:
                result += int(digit)
            num = result
        return num    
