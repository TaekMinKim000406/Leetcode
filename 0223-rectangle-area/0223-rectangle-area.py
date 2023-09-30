class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        a = (ax1, ay1, ax2, ay2)
        b = (bx1, by1, bx2, by2)
        x = 0
        y= 0
        if a[0]<=b[0]<=b[2]<=a[2]:
            x = b[2]-b[0]
        elif b[0]<=a[0] <=a[2] <=b[2]:
            x = a[2]-a[0] 
        elif a[0]<b[2]<a[2]:
            x= b[2]-a[0]
        elif b[0]<a[2]<b[2]:
            x= a[2]-b[0]   
        
        if a[1]<=b[1]<=b[3]<=a[3]:
            y = b[3]-b[1]
        elif b[1]<=a[1] <=a[3] <=b[3]:
            y = a[3]-a[1] 
        elif a[1]<b[3]<a[3]:
            y= b[3]-a[1]
        elif b[1]<a[3]<b[3]:
            y=a[3]-b[1]   

        print(x*y)

        return (a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-x*y