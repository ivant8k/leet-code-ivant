class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = board[row][col]
                    rows[row].add(num)
                    cols[col].add(num)
                    subgrids[(row // 3) * 3 + (col // 3)].add(num)

        def isValid(row, col, num):
            subgrid_index = (row // 3) * 3 + (col // 3)
            if num in rows[row] or num in cols[col] or num in subgrids[subgrid_index]:
                return False
            return True

        def placeNumber(row, col, num):
            board[row][col] = num
            rows[row].add(num)
            cols[col].add(num)
            subgrids[(row // 3) * 3 + (col // 3)].add(num)

        def removeNumber(row, col, num):
            board[row][col] = "."
            rows[row].remove(num)
            cols[col].remove(num)
            subgrids[(row // 3) * 3 + (col // 3)].remove(num)

        def findEmptyCell():
            min_options = float('inf')
            best_cell = None
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        options = 0
                        for n in range(1, 10):
                            num = str(n)
                            if isValid(row, col, num):
                                options += 1
                        if options < min_options:
                            min_options = options
                            best_cell = (row, col)
            return best_cell

        def solve():
            cell = findEmptyCell()
            if not cell:
                return True
            row, col = cell
            for n in range(1, 10):
                num = str(n)
                if isValid(row, col, num):
                    placeNumber(row, col, num)
                    if solve():
                        return True
                    removeNumber(row, col, num)
            return False

        solve()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solution = Solution()
solution.solveSudoku(board)

for row in board:
    print(row)