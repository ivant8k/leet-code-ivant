class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        def backtrack(path, remaining):
            if not remaining:
                ans.append(path)
                return
            prev = None
            for i in range(len(remaining)):
                if remaining[i] == prev:
                    continue
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
                prev = remaining[i]

        backtrack([], nums)
        return ans
    
solution = Solution()
print(solution.permuteUnique([1, 1, 2]))
print("-"*10)
print(solution.permuteUnique([1, 2, 3]))