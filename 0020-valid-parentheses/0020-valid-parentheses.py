class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True 
        stack = []
        for i in range(len(s)):
            if (s[i] in ['(','{','[']):
                stack.append(s[i])
            elif (s[i] == '}'):
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif (s[i] == ')'):
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif (s[i] == ']'):
                if len(stack) == 0 or stack.pop() != '[':
                    return False

        if len(stack)!=0:
            return False

        return True;        
