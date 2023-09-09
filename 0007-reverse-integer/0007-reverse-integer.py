class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
 

        isPositive = True
        if x < 0:
            isPositive = False
        x = str(x)

        if isPositive:
            x = x[::-1]
        else:
            x = x[1::]
            x = x[::-1]   

        for i in range(len(x)):
            if x.startswith('0'):
                x = x[1::]
            else:
                break    
        print(x)  

        if len(x) == 0:
            return 0


        if isPositive:
            x= int(x)
        else:
            x= int('-'+x) 

        if -(2**31)>x or x> (2**31) -1:
            return 0
        else:
            return x           