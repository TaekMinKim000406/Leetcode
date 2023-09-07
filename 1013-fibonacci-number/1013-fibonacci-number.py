class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #메모리 부족
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 1
        # else:
        #     return self.fib(n-1)+self.fib(n-2)
        if n == 1:
            return 1
        elif n == 2:
            return 1   
        num = 0
        bef1=1
        bef2=1     
        for i in range(n):
            if i == 0 or i ==1:
                num +=1
            else:
                num=bef1+bef2
                bef1=bef2
                bef2=num
        return num

