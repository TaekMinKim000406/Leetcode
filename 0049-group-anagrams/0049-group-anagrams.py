class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        new_strs = []
        indexes = {}

        for i in range(len(strs)):
            new_strs.append(sorted(strs[i]))

        for i in range(len(new_strs)):
            if str(new_strs[i]) in indexes.keys():
                indexes[str(new_strs[i])] += [i]
            else:
                indexes[str(new_strs[i])] = [i]

        result = []
        for index, value in indexes.items():
            result.append([strs[x] for x in value])
        return result
