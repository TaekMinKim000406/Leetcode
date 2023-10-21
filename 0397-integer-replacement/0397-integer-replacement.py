class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        best_value = [99999999]
        def rcsv(n, cost):
            if cost>best_value[0]:
                return
            if n == 1:
                best_value[0] = min(best_value[0], cost)
            elif n%2==0:
                rcsv(n//2,cost+1)
            else:
                rcsv(n+1, cost+1)
                rcsv(n-1, cost+1)    
        rcsv(n,0)
        return best_value[0]