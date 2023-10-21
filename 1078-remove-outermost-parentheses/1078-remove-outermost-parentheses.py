class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = 0
        indexes = []
        while index<len(s):
            st = 1
            next = index+1 #index는 반드시 (여야 한다.
            while True:
                if s[next] == ')':
                    st-=1
                elif s[next] == '(':    
                    st+=1
                if st == 0:
                    break
                else:
                    next+=1    
            indexes.append(index)
            indexes.append(next)
            index = next+1
        # print(indexes)
        s = list(s)
        for i in range(len(indexes)-1,-1,-1):
            s.pop(indexes[i])
        return ''.join(s)

