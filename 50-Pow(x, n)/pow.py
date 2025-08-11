class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.00000
        
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.00000
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result

solution = Solution()
print(solution.myPow(2.00000, 10))  # 1024.
print(solution.myPow(2.10000, 3))   # 9.261
print(solution.myPow(2.00000, -2))  # 0.250