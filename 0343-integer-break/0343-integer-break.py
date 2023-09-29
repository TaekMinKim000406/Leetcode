class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_value = 0
        for k in range(2,n+1):
            val = int(n/k)
            remain = n%k
            values = [val for _ in range(k)]
            for i in range(remain):
                values[i]+=1
            value = 1
            for num in values:
                value*=num
            max_value = max(max_value, value)
        return max_value    