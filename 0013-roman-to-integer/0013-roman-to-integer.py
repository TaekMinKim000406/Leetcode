class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)):
            if (i>0) and s[i-1:i+1] in ["CM", "CD", "XL", "XC", "IX", "IV"]:
                continue
            if s[i]=='I':
                if (i==len(s)-1):
                    count+=1
                else:    
                    if (s[i+1]=='V'):
                        count+=4
                    elif (s[i+1]=='X'): 
                        count+=9
                    else:
                        count+=1    
            elif (s[i]=='V'):
                    count+=5
            elif (s[i]=='X'):
                if (i==len(s)-1):
                    count+=10
                else:
                    if (s[i+1]=='L'):
                        count+=40
                    elif (s[i+1]=='C'): 
                        count+=90
                    else:
                        count+=10
            elif (s[i]=='L'):
                count+=50
            elif (s[i]=='C'):
                if (i==len(s)-1):
                    count+=100
                else:
                    if (s[i+1]=='D'):
                        count+=400
                    elif (s[i+1]=='M'):
                        count+=900
                    else:
                        count+=100
            elif (s[i]=='D'):
                count+=500
            elif (s[i]=='M'):
                count+=1000                        
        return count
        