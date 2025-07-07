class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        board = [ ["."] * n for _ in range(n) ]
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)  # row + col
        diag2 = [False] * (2 * n - 1)  # row - col + n - 1

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return
            for col in range(n):
                d1 = row + col
                d2 = row - col + n - 1
                if not cols[col] and not diag1[d1] and not diag2[d2]:
                    board[row][col] = "Q"
                    cols[col] = diag1[d1] = diag2[d2] = True
                    backtrack(row + 1)
                    board[row][col] = "."
                    cols[col] = diag1[d1] = diag2[d2] = False

        backtrack(0)
        return len(ans)
    
solution = Solution()
print(solution.totalNQueens(4))