class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num:
                    return False
                
            for y in range (9):
                if board[y][col] == num:
                    return False
            
            startRow = 3 * (row // 3)
            startCol = 3 * (col // 3)

            for i in range (3):
                for j in range (3):
                    if board[i + startRow][j + startCol] == num:
                        return False
            return True

        def solve():
            for row in range(9):
                for col in range (9):
                    if board[row][col] == ".":
                        for n in range (1,10):
                            num = str(n)
                            if isValid(board,row,col,num):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = "."
                        return False
            return True

        solve()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solution = Solution()
solution.solveSudoku(board)

for row in board:
    print(row)