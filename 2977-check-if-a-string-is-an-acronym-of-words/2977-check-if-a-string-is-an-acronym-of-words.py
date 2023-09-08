class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        s2 = ""
        for i in range(len(words)):
            sen = words[i]
            s2 += sen[0]

        print(s2)   
        if s2 == s:
            return  True
        else:
            return False        
        