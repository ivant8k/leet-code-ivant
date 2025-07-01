# n = 32
# p = 2
# while p * p <= n:
#     print("\n+p = ", p)
#     for i in range(p * p, n + 1, p):
#         print(i, end=' ')
#     p+= 1

# Sieve of Eratosthenes to count primes less than n
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True] * (n+1)
        p = 2

        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        
        count = 0
        for p in range(2, n):
            if prime[p]:
                count += 1
        return count
    
# sol = Solution()
# print(sol.countPrimes(10))
