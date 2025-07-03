class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        return triangle[0][0]
    
solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # Output: 11
print(solution.minimumTotal([[-10]]))  # Output: -10
print(solution.minimumTotal([[-1],[2,3],[1,-1,-3]]))  # Output: -1