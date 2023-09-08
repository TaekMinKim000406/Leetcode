class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s =""
        for alpah in s:
            if (alpah >= 'a' and alpah<='z') or(alpah >= 'A' and alpah<='Z') or (alpah >= '0' and alpah<='9'):
                new_s+=alpah

        new_s= new_s.lower()
        reversed_s = new_s[::-1]

        if new_s == reversed_s:
            return True
        else:
            return False    