class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        k=0
        if len(flowerbed)<2:
            if flowerbed[0]==0:
                k=1
            else:
                k=0   
        else:
            for i in range(len(flowerbed)):
                if i==0:
                    if flowerbed[i]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        k+=1
                if i==len(flowerbed)-1:
                    if flowerbed[i]==0 and flowerbed[i-1]==0:
                        flowerbed[i]=1
                        k+=1      
                if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    k+=1
    
        if n<=k:
            return True
        else:
            return False    