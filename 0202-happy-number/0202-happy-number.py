class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = []

        while True:
            if n in visited:
                return False
            if n == 1:
                return True
            visited.append(n)
            n = str(n)
            result = 0
            for i in range(len(n)):
                result += int(n[i])*int(n[i])
            n = result
            




        