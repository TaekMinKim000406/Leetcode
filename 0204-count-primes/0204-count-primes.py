class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
        
        # if n < 2:
        #     return 0
        # prime_list = []
        # for i in range(2, n):
        #     is_prime = True
        #     for prime in prime_list:
        #         if i % prime == 0:
        #             is_prime = False
        #             break
        #     if is_prime:
        #         prime_list.append(i)

        # return len(prime_list)