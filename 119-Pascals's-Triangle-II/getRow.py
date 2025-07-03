class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        mat = []

        for row in range(rowIndex + 1):
            arr = []
            for i in range (row + 1):
                if row == i or i == 0:
                    arr.append(1)
                else:
                    arr.append(mat[row - 1][i - 1] + mat[row - 1][i])
            mat.append(arr)
        return mat[rowIndex]

solution = Solution()
print(solution.getRow(3))  # Output: [1, 3, 3, 1]
print(solution.getRow(0))  # Output: [1]
print(solution.getRow(1))  # Output: [1,1]