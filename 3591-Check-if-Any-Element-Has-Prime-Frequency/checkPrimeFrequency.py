class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def isPrime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        for i in nums:
            if nums.count(i) > 1 and isPrime(nums.count(i)):
                return True
        return False
            
solution = Solution()
print(solution.checkPrimeFrequency([1,2,3,4,5,4]))
print(solution.checkPrimeFrequency([1,2,3,4,5]))
print(solution.checkPrimeFrequency([2,2,2,4,4]))