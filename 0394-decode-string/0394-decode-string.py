class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_list = []
        index = 0

        while index<len(s):
            if s[index].isdigit():
                start_index = index
                while s[index].isdigit():
                    index+=1
                num = int(s[start_index:index])
                stack_list.append(num)
            elif s[index] == '[':
                stack_list.append('[')
                index +=1
            elif s[index] == ']':
                stack_list.append(']')
                index +=1
            else:
                start_index = index
                while index<len(s) and s[index] != ']' and not  s[index].isdigit() :
                    index+=1
                stack_list.append(str(s[start_index:index]))   
 


        while '[' in stack_list:
            for i in range(len(stack_list)-1):  
                if stack_list[i] == '[': 
                    flag = False
                    for j in range(i+1, len(stack_list)):
                        if stack_list[j] == ']':
                            flag = j
                            break
                        if stack_list[j] == '[':
                            break
                    if flag:
                        ele = ''
                        for k in range(i+1, flag):
                            ele+=stack_list[k]
                        ele = ele * stack_list[i-1]    
                        stack_list = stack_list[:i-1]+[ele]+stack_list[flag+1:]
                        break
                        
        result = ''
        for i in range(len(stack_list)):
            result += stack_list[i]
        return result    
        # return sum(stack_list)        

