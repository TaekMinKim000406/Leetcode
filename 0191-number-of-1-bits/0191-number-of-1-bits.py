class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_bit = ''
        count = 0
        while n>0:
            # binary_bit+= str(n%2)
            if n%2==1:
                count+=1
            n//=2

        # binary_bit = binary_bit[::-1]
        return count
        # print(binary_bit)