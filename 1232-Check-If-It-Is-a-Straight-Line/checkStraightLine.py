class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        dx0 = coordinates[1][0] - coordinates[0][0]
        dy0 = coordinates[1][1] - coordinates[0][1]
        for i in range(2, len(coordinates)):
            dx = coordinates[i][0] - coordinates[0][0]
            dy = coordinates[i][1] - coordinates[0][1]
            if dx * dy0 != dy * dx0:
                return False
        return True
    
solution = Solution()
print(solution.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  # True
print(solution.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))  # False