class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #그림 보면 나오는데 대충 각 행의 첫 원소는 첫 번째 줄로, 두 번째 원소는 두번째 줄임 (쉽게 생각해서 행과 열을 바꾸고 나서 역으로 정렬하면 됨)
        n = len(matrix)
      
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i>=j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]  
                    matrix[j][i] = temp 
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
