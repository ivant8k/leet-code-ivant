class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # Backtracking approach
        # ans = []
        # board = [["."] * n for _ in range(n)]

        # def is_valid(row, col):
        #     for i in range (row):
        #         # Check column
        #         if board[i][col] == "Q":
        #             return False
        #         # Check left diagonal
        #         if col - (row - i) >= 0 and board[i][col - (row - i)] == "Q":
        #             return False
        #         # Check right diagonal
        #         if col + (row - i) < n and board[i][col + (row - i)] == "Q":
        #             return False
        #     return True 
        
        # def backtrack(row):
        #     if row == n:
        #         ans.append(["".join(r) for r in board])
        #         return
            
        #     for col in range(n):
        #         if is_valid(row, col):
        #             board[row][col] = "Q"
        #             backtrack(row + 1)
        #             board[row][col] = "."
        # backtrack(0)
        # return ans

        # Branch and Bound approach
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
        return ans
        
solution = Solution()
print(solution.solveNQueens(4))
# print(solution.solveNQueens(1))