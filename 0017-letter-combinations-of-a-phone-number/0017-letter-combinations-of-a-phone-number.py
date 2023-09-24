class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def translate(number):
            if number == '2':
                return 'abc'
            elif number == '3':
                return 'def'  
            elif number == '4':
                return 'ghi' 
            elif number == '5':
                return 'jkl' 
            elif number == '6':
                return 'mno' 
            elif number == '7':
                return 'pqrs' 
            elif number == '8':
                return 'tuv' 
            elif number == '9':
                return 'wxyz' 

        if len(digits)==0:
            return

        result = []
        first=translate(digits[0])
        for st in first:
            result.append(st)   

        for i in range(1,len(digits)):
            next_letters = translate(digits[i]) 
            new_letters = []
            for next_letter in next_letters:
                last_letters= result[:]
                for j in range(len(last_letters)):
                    new_letters.append(last_letters[j]+ next_letter)               
            result = new_letters
            
        return result    

        