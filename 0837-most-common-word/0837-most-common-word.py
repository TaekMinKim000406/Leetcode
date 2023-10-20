class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # paragraph=paragraph.replace('.', ' ')
        # paragraph=paragraph.replace(',', ' ')
        # paragraph=paragraph.replace('!', ' ')
        # paragraph=paragraph.replace('?', ' ')
        # paragraph=paragraph.replace(';', ' ')

 

        paragraph = paragraph.lower()
        
        for i in range(len(paragraph)):
            if paragraph[i].isalnum() or paragraph[i].isspace():
                continue
            else:
                paragraph = paragraph[:i]+' ' +paragraph[i+1:]  


        words = list(paragraph.split())
        
        # print(words)
        words = [word for word in words if word not in banned]
        # print(words)
        dic = {}
        for word in words:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
        # print(dic)            
        max_key = max(dic, key=dic.get)
        return max_key