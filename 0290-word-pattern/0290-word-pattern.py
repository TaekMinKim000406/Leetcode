class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()

        if len(s)!= len(pattern):
            return False

        word = {}

        for i in range(len(pattern)):
            if pattern[i] in word:
                if word[pattern[i]] == s[i]:
                    continue
                else:
                    return False
            else:
                word[pattern[i]] = s[i]   

        words = []
        for key, value in word.items():
            if value in words:
                return False
            else:
                words.append(value)     



        return True

