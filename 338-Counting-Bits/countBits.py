class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
    
solution = Solution()
print(solution.countBits(2))  # Output: [0, 1, 1]
print(solution.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]