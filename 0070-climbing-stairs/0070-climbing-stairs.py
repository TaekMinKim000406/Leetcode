class Solution(object):
    def factorial(self, n):
        if n==1:
            return 1    
        return n*self.factorial(n-1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2x + y = n
        k=0
        for i in range(n//2+1):
            num2= i
            num1 = n-2*i
            if num1 == 0:
                k+=1
                continue
            elif num2 == 0:
                k+=1
            else:
                k+= (self.factorial((num1+num2))/self.factorial(num1)/self.factorial(num2))
        return k        