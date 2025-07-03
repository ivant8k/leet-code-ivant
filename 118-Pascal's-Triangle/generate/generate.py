class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        mat = []

        for row in range(numRows):
            arr = []
            for i in range (row + 1):
                if row == i or i == 0:
                    arr.append(1)
                else:
                    arr.append(mat[row - 1][i - 1] + mat[row - 1][i])
            mat.append(arr)
        return mat

solution = Solution()
print(solution.generate(5))
print(solution.generate(1))