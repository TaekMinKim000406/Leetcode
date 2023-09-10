class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s and s[0]==' ' :
            s = s[1:]

        isstr= False
        while s and s[0].isalpha():
            s = s[1:]
            isstr = True
        if isstr and s and s[0]!=' ':
           return 0     

        result = ''
        if s and (s[0] == '-' or s[0] == '+'):
            result += s[0]
            s = s[1:]
        while s and s[0].isdigit():
            result+=s[0]
            s = s[1:]

        print(result)

        try:       
            if result == '':
                return 0
            elif int(result)<-2**31:
                return -2147483648
            elif int(result)>2**31-1:
                return 2147483647
            else:            
                return int(result)
        except:
            return 0        