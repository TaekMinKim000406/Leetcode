class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        isPositive = True
        if num < 0:
            isPositive=False
            num *= -1
        elif num == 0:
            return '0'

        result = ''

        while num > 0:
            result += str(num%7)
            num //= 7    
        if not isPositive:
            result += '-'

        result = result[::-1]
        return result
        # max_value = 1
        # while max_value <= num:
        #     max_value*=7
        # max_value = int(max_value/7)
        
        # result = ''
        # if not isPositive:
        #     result += '-'
            
        

        # while max_value >= 1:
        #     result += str(num//max_value)
        #     num %= max_value
        #     max_value = int(max_value/7)
            
        # return result





        