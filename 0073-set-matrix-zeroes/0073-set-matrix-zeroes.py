class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = [False]* len(matrix)
        columns = [False] * len(matrix[0])
        

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    rows[i]=True
                    columns[j]=True

        for i in range(len(matrix)):
            if rows[i]==True:
                for j in range(len(matrix[i])):
                    matrix[i][j]=0

        for j in range(len(matrix[0])):
            if columns[j]==True:
                for i in range(len(matrix)):
                    matrix[i][j]=0

        print(columns)
        print(rows)

