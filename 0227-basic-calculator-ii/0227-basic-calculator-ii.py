class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        state = -1
        cur = 0
        nums = []
        oprs = []
        for i in range(len(s)):
            if '0'<=s[i]<='9':
                if state != 0:
                    state = 0
                    cur = int(s[i])    
                else:
                    cur = cur*10+ int(s[i])
            elif s[i]==' ':
                continue          
            else:
                state = 1
                nums.append(cur)
                oprs.append(s[i])
        nums.append(cur)
        # print(nums, oprs)

        i=0
        while i<len(oprs):
            if oprs[i] == '*':
                nums[i] *= nums[i+1]
                nums.pop(i+1)
                oprs.pop(i)
            elif oprs[i] == '/':
                nums[i] /= nums[i+1]
                nums.pop(i+1)
                oprs.pop(i)
            else:
                i+=1    

        print(nums, len(oprs)) 
        result = nums[0]
        for i in range(len(oprs)):
            if oprs[i]=='+':
                result += nums[i+1]
            else:
                result -= nums[i+1]
        return result            

        