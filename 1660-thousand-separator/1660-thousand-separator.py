class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = list(str(n))
        index = len(result)-1
        count = 0
        while index>=0:
            count+=1
            if count==3:
                result.insert(index,'.')
                count=0
            index-=1
        # print(result)        

        if result[0]=='.':
            result.pop(0)

        return ''.join(result)    



        # result = str(n%1000)
        # while n>=1000:
        #     n //=1000
        #     result = str(n%1000)+'.'+result
            

        # return result

