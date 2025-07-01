class Solution(object):
    def plusOne(self, digits):
        str_digits = ''.join(str(i) for i in digits)
        int_digits = int(str_digits) + 1
        str_digits2 = str(int_digits)
        return list(map(int,str_digits2))