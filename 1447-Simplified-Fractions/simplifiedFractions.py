class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                print(f"Checking fraction {numerator}/{denominator}...")
                print(f"GCD of {numerator} and {denominator} is {gcd(numerator, denominator)}")
                if gcd(numerator, denominator) == 1:
                    # result.append(f"{numerator}/{denominator}")
                    result.append(str(numerator) + '/' + str(denominator))
        return result
    
# Example usage:
solution = Solution()
print(solution.simplifiedFractions(2))
print(solution.simplifiedFractions(3))
print(solution.simplifiedFractions(4))

