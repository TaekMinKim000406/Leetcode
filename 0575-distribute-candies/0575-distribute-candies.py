class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        typeNum =  len(set(candyType))
        return min(typeNum, len(candyType)//2)        
