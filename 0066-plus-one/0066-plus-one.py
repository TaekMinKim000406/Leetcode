class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        array=[]
        for i in range(len(digits)):
            num += str(digits[i])
        num = str(int(num)+1)
        for i in range(len(num)):
           array.append(int(num[i]))
        return array   

        