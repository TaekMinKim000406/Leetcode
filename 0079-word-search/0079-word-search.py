class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # m=len(board)
        # n=len(board[0])
        # def find(character,board, cur_x, cur_y):
        #     index_list = []
        #     if cur_x>0:
        #         if board[cur_x-1][cur_y] == character:
        #             index_list.append([cur_x-1,cur_y])
        #     if cur_x<m-1:
        #         if board[cur_x+1][cur_y] == character:
        #             index_list.append([cur_x+1,cur_y])
        #     if cur_y>0:
        #         if board[cur_x][cur_y-1] == character:
        #             index_list.append([cur_x,cur_y-1])
        #     if cur_y<n-1:    
        #         if board[cur_x][cur_y+1] == character:
        #             index_list.append([cur_x,cur_y+1])
        #     return index_list 

        # visited=[]
        # def find_pattern(word, board, cur_x, cur_y):
        #     result = find(word[0], board, cur_x, cur_y)
        #     visited.append([cur_x, cur_y])
        #     if [0,3] in visited:
        #         print(visited)

        #     for x,y in visited:
        #         if [x,y] in result:
        #             result.remove([x,y])

        #     if len(result)==0:
        #         return False

        #     if len(word)==1:
        #         return True

        #     for i in range(len(result)):
        #         bools.append(find_pattern(word[1:], board, result[i][0], result[i][1]))

        #     if True in bools:
        #         return True
        
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j]==word[0]:
        #             visited = []
        #             if len(word)==1:
        #                 return True
        #             if find_pattern(word[1:], board, i,j):
        #                 return True
        # return False                
        m = len(board)
        n = len(board[0])

        def backtrack(cur_x, cur_y, index):
            # 단어를 모두 찾았을 때
            if index == len(word):
                return True

            # 현재 위치가 유효한지 확인
            if (
                cur_x < 0
                or cur_x >= m
                or cur_y < 0
                or cur_y >= n
                or board[cur_x][cur_y] != word[index]
            ):
                return False

            # 현재 위치의 문자를 임시로 저장하고 해당 위치를 방문했음을 표시
            temp = board[cur_x][cur_y]
            board[cur_x][cur_y] = "#"

            # 상하좌우 방향으로 재귀 호출
            found = (
                backtrack(cur_x + 1, cur_y, index + 1)
                or backtrack(cur_x - 1, cur_y, index + 1)
                or backtrack(cur_x, cur_y + 1, index + 1)
                or backtrack(cur_x, cur_y - 1, index + 1)
            )

            # 현재 위치를 원래 값으로 되돌림
            board[cur_x][cur_y] = temp

            return found

        # 보드의 모든 위치에서 시작해보며 단어를 찾음
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False

