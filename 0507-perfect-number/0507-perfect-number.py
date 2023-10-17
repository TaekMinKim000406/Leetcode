class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        divisor = []
        for i in range(1, int(num**0.5)+1):
            if num%i==0:
                divisor.append(i)
                divisor.append(num//i)
        divisor.remove(num)


        if sum(divisor) == num:
            return True
        else:
            return False            
        