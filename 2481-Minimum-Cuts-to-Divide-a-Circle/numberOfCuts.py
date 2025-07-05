class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 0:
            return n // 2
        else:
            return n if n > 1 else 0
        
solution = Solution()
print(solution.numberOfCuts(4))  # Output: 2
print(solution.numberOfCuts(3))  # Output: 3