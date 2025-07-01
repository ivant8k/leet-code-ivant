class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True
        
# solution = Solution()
# print(solution.canWinNim(4))
# print(solution.canWinNim(1))
# print(solution.canWinNim(2))