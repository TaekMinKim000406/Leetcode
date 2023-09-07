class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            array=[]
            for i in range(numRows):
                if i == 0:
                    array.append([1])
                elif i == 1:
                    array.append([1,1])
                else:
                    result = []
                    result.append(1)
                    for j in range(i-1):
                        result.append(array[i-1][j]+array[i-1][j+1])
                        # result.append(2)
                    result.append(1)    
                    array.append(result)
            return array
        