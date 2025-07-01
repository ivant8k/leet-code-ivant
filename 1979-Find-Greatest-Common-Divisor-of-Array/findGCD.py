class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        max_num = max(nums)

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        return gcd(min_num, max_num)
    
# Example usage:
solution = Solution()
print(solution.findGCD([2, 5, 6, 9, 10]))
print(solution.findGCD([7, 5, 6, 8, 3]))