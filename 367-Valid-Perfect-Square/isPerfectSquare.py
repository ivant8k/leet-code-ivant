class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num == 0 or num == 1:
            return True
        
        last_digit = num % 10
        if last_digit in [2, 3, 7, 8]:
            return False
        
        # Binary search approach
        low = 1
        high = num

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square < num:
                low = mid + 1
            elif square > num:
                high = mid - 1
            else:
                return True
        return False

        # Linear search approach
        # low = 1
        # high = num // 2 + 1

        # while low <= high:
        #     if low * low == num:
        #         return True
        #     else:
        #         low += 1
        # return False
    
solution = Solution()
print(solution.isPerfectSquare(16))  # Output: True
print(solution.isPerfectSquare(14))  # Output: False
