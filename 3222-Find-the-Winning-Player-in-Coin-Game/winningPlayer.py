class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        def canPickCoins(x, y):
            return x > 0 and y >= 4

        turn = 0
        while canPickCoins(x, y):
            x -= 1
            y -= 4
            turn = 1 - turn

        return "Bob" if turn == 0 else "Alice"

solution = Solution()
print(solution.winningPlayer(2, 7))  # Output: "Alice"
print(solution.winningPlayer(4, 11))  # Output: "Bob"
print(solution.winningPlayer(1, 1))  # Output: "Bob"
print(solution.winningPlayer(2, 1))  # Output: "Bob"