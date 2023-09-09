class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        start = 0
        char_dict = {} #key=char: value=index(integer)
        for i in range(len(s)):
            if s[i] in char_dict and char_dict[s[i]]>=start:
                start = char_dict[s[i]]+1
            else:
                max_length = max(max_length, i-start+1)
            char_dict[s[i]] = i
        return max_length             