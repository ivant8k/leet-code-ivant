class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # result = []
        n = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                # result.append(i)
                n+= 1
        return n
    
# solution = Solution()
# print(solution.commonFactors(12, 6))
# print(solution.commonFactors(25, 30))
