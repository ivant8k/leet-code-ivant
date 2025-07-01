class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return ''.join(result[::-1])

# solution = Solution()
# print(solution.addBinary("11", "1"))  # Output: "100"
# print(solution.addBinary("1010", "1011"))  # Output: "10101"