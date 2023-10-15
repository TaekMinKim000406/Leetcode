class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if abs(rec1[3]-rec1[1])+ abs(rec2[3]-rec2[1]) > max(rec1[3],rec1[1], rec2[3],rec2[1])-min(rec1[3],rec1[1], rec2[3],rec2[1]) and abs(rec1[2]-rec1[0])+ abs(rec2[2]-rec2[0]) > max(rec1[2],rec1[0], rec2[2],rec2[0])-min(rec1[2],rec1[0], rec2[2],rec2[0]):
            return True
        else:
            return False    