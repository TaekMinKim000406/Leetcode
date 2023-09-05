class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max_num=-1
        min_index=0
        prefix = None
        for i in range(len(strs)):
            if len(strs[i])<len(strs[min_index]):
                min_index = i

        for i in range(len(strs[min_index])):
            flag = True
            for j in range(len(strs)):
                if strs[min_index][i] != strs[j][i]:
                    flag=False
                    break                        
            if flag:
                max_num = i
            else:
                break    


        return strs[min_index][:max_num+1:]