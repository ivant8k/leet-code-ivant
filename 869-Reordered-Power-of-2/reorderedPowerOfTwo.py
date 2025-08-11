class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from collections import Counter

        nCount = Counter(str(n))
        for i in range(31):  # 2^0 to 2^30
            powerOfTwoCount = Counter(str(1 << i))  # 1 << i
            if nCount == powerOfTwoCount:
                return True
        return False
    
solution = Solution()
print(solution.reorderedPowerOf2(1))  # True
print(solution.reorderedPowerOf2(10))  # False