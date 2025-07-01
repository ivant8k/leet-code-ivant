class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 == 0:
            return True
        else:
            return False
        
# solution = Solution()
# print(solution.divisorGame(2))  # True
# print(solution.divisorGame(3))  # False