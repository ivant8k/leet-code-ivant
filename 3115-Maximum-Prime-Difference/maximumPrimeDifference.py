class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isPrime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        primes_index = [i for i in range(len(nums)) if isPrime(nums[i])]
        return primes_index[len(primes_index) - 1] - primes_index[0]

solution = Solution()
print(solution.maximumPrimeDifference([4,2,9,5,3]))