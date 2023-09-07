class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sort_s = sorted(list(s))
        sort_t = sorted(list(t))
        if sort_s == sort_t:
            return True
        else:
            return False    
