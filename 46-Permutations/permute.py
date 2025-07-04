class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans, sol = [], []

        def backtrack():
            if len(sol) == len(nums):
                ans.append(sol[:])
                return
            
            for i in range (len(nums)):
                if nums[i] in sol:
                    continue
                sol.append(nums[i])
                backtrack()
                sol.pop()
        
        backtrack()
        return ans
    
solution = Solution()
print(solution.permute([1, 2, 3]))
print(solution.permute([0, 1]))
print(solution.permute([1]))
        