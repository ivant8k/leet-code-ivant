class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky = -1
        for num in set(arr):
            if arr.count(num) == num:
                lucky = max(lucky, num)
        return lucky
    
solution = Solution()
print(solution.findLucky([2,2,3,4]))  # 2
print(solution.findLucky([1,2,2,3,3,3]))  # 3
print(solution.findLucky([5,4,7,8,4,8,8,3,7,7,6,3,7,6,5,6,8,4,5,7,4,7,7,5,2,5,6,6,8,1,6,8,8,8,9,3,2,9]))  # 8