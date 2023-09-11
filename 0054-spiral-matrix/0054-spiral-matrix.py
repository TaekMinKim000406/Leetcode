class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_length = len(matrix)
        column_length = len(matrix[0])
        top_to_bottom=False
        bottom_to_top=False
        left_to_right=True
        right_to_left=False
        column,row = 0,0       
        visit = [[0] * column_length for _ in range(row_length)]
        result = []
        for i in range(row_length*column_length):
            visit[row][column]=1
            result.append(matrix[row][column])
            if left_to_right:
                if column == column_length-1 or visit[row][column+1] !=0:
                    left_to_right = False
                    top_to_bottom = True
                    row+=1
                else:
                    column +=1
            elif right_to_left:
                if column == 0 or visit[row][column-1] !=0:
                    right_to_left = False
                    bottom_to_top = True
                    row-=1
                else:
                    column -=1
            elif top_to_bottom:
                if row == row_length-1 or visit[row+1][column] !=0:
                    top_to_bottom = False
                    right_to_left = True
                    column-=1
                else:
                    row +=1
            elif bottom_to_top:
                if row == 0 or visit[row-1][column] !=0:
                    bottom_to_top = False
                    left_to_right = True
                    column+=1
                else:
                    row -=1                   
        return result