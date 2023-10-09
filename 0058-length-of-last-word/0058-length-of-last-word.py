class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s[-1]==' ':
            s = s[:-1]

        for i in range(len(s)):
            if s[len(s)-1-i] == ' ':
                return i
        return len(s)        