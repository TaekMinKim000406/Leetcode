class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #4개의 변수로 해결 가능(top, bottom, left, right)
        top_to_bottom=False
        bottom_to_top=False
        left_to_right=True
        right_to_left=False
        column,row = 0,0       
        result = [[0] * n for _ in range(n)]

        for i in range(n*n):
            result[row][column]=i+1
            if left_to_right:
                if column == n-1 or result[row][column+1] !=0:
                    left_to_right = False
                    top_to_bottom = True
                    row+=1
                else:
                    column +=1
            elif right_to_left:
                if column == 0 or result[row][column-1] !=0:
                    right_to_left = False
                    bottom_to_top = True
                    row-=1
                else:
                    column -=1
            elif top_to_bottom:
                if row == n-1 or result[row+1][column] !=0:
                    top_to_bottom = False
                    right_to_left = True
                    column-=1
                else:
                    row +=1
            elif bottom_to_top:
                if row == 0 or result[row-1][column] !=0:
                    bottom_to_top = False
                    left_to_right = True
                    column+=1
                else:
                    row -=1                   
        return result


    #     def generateMatrix(self, n):
    # A, lo = [], n*n+1
    # while lo > 1:
    #     lo, hi = lo - len(A), lo
    #     A = [range(lo, hi)] + zip(*A[::-1])
    # return A
