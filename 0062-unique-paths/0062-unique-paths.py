class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #메모리 초과됨
        # def nextMove(path, left_m, left_n, path_array = []):

        #     if left_m>0 and left_n>0:
        #         nextMove(path+'R', left_m-1, left_n)
        #         nextMove(path+'B', left_m, left_n-1)
        #     else:
        #         path_array.append(path)
        #     return path_array
    
        # unique_path = nextMove('',m-1,n-1)
        # return len(unique_path)


        def factorial_recursive(n):
            if n == 0:
                return 1
            else:
                return n * factorial_recursive(n - 1)
        return factorial_recursive(m+n-2)/factorial_recursive(m-1)/factorial_recursive(n-1)