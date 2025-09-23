class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_good_integer = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                current_good_integer = num[i] * 3
                if current_good_integer > max_good_integer:
                    max_good_integer = current_good_integer
        return max_good_integer
    
solution = Solution()
print(solution.largestGoodInteger("6777133339"))  # "777"
print(solution.largestGoodInteger("2300019"))     # "000"
print(solution.largestGoodInteger("123"))         # ""