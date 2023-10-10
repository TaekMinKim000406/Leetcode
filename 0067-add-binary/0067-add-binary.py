class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        while len(a)>len(b):
            b = '0'+b

        while len(b)>len(a):
            a = '0'+a
        
        a = a[::-1]
        b = b[::-1]

        mid = [0 for _ in range((len(a)+1))]
        result = ''
        for i in range(len(a)):
            cur = int(a[i])+int(b[i])+mid[i]
            if cur <= 1:
                result+=str(cur)
            else:
                mid[i+1]=1
                result+=str(cur-2)
        if mid[-1]==1:            
            result += '1'
        return result[::-1]    

        # #실수
        # num = int(a)+int(b)
        # i = 0
        # while True:
        #     if 2**i>num:
        #         break
        #     i+=1    
        # i-=1
        # result = ''
        # for j in range(i,0,-1):
        #     if num>2**i:
        #         result+='1'
        #         num-=2**i
        #     else:
        #         result+='0'
        # return result

        