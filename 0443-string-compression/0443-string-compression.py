class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index = 0
        while index < len(chars):
            sames = index+1
            while sames<len(chars) and chars[sames] == chars[index]:
                sames+=1
            count = sames - index

            if count >1:
                for i in range(count-1):
                    chars.pop(index+1)
                if count<10:
                    chars.insert(index+1, str(count))
                    index +=1
                else:
                    count = str(count)
                    for i in range(len(count)):
                        chars.insert(index+1, count[len(count)-1-i]) 
                    index += len(count)
            index+=1               
            







        # index = 0
        # char = []
        # nums = []
        # while index < len(chars):
        #     if char and char[-1] == chars[index]:
        #         nums[-1]+=1
        #     else:
        #         char.append(chars[index])
        #         nums.append(1)
        #     index+=1
        # print(char)
        # print(nums)
        # nums = [num for num in nums if num != 1]

        # return len(char)+len(nums)            



