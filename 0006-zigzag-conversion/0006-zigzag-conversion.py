class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        sen = [""] * numRows
        row , column = 0,0
        for i in range(len(s)):
            sen[row] += s[i]
            if column % (numRows-1) ==0:
                row +=1
                if row == numRows:
                    row-=2
                    column +=1
            else:
                row -= 1
                column+=1

        result = ''
        for i in range(len(sen)):
            result +=sen[i]
        return result