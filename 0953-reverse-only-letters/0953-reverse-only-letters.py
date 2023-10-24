class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s)-1
        while start <= end:
            if not s[start].isalpha():
                start+=1
            elif not s[end].isalpha():    
                end -=1
            else:
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1

        return ''.join(s)                

