def expand(s,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return s[i+1:j] 
class Solution(object):
   
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if len(s) ==1:
        #     return s
        # dict_s = {}
        # for i in s:
        #     if i in dict_s:
        #         dict_s[i] +=1
        #     else:        
        #         dict_s[i] = 1
        # for key, value in dict_s.items():
        #     if value == 1:
        #         del dict_s[key]

        # length = 0
        # output = ''
        # for i in range(len(s)):
        #     if s[i] in dict_s:
        #         for j in range(len(s)-i):
        #                 substring = s[i:i+j+1]
        #                 if substring== substring[::-1]:
        #                     if length<len(substring):
        #                         output = substring
        #                         length=len(substring)

        # if length<=1:
        #     return s[0]

        # return output
        
        # max_length = -1
        # output = ''
        # #case 1: 중간에 문자 하나를 기준으로 양쪽이 대칭
        # for i in range(len(s)): #i=3
        #     for j in range(i+1): #j=1
        #         substring = s[i-j:i+j+1] 
        #         if substring == substring[::-1]:
        #             if len(substring)>max_length:
        #                 max_length =len(substring)
        #                 output = substring

        # #case 2: 중간에 같은 문자 2개를 기준으로 양쪽 대칭
        # for i in range(len(s)-1): #i=1
        #     if s[i]==s[i+1]:
        #         for j in range(i+1): #j=1
        #             substring = s[i-j:i+j+2] 
        #             if substring == substring[::-1]:
        #                 if len(substring)>max_length:
        #                     max_length =len(substring)
        #                     output = substring
        # return output
        ans=''
        for i in range(len(s)):
            ans=max(ans,expand(s,i,i), expand(s,i,i+1), key=len)
        return ans
