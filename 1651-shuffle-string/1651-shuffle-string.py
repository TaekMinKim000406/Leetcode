class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        lis = []
        for num in range(len(indices)):
            lis.append([indices[num], s[num]])

        lis.sort()
        print(lis)
        result = ''
        for i in range(len(lis)):
            result += lis[i][1]


        return result
