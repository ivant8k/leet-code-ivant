class Solution(object):
    def isPalindrome(self, x):
        if x<0:
         return False
        
        balik = 0
        simpan = x
        while simpan != 0:
            digit = simpan%10
            balik = balik*10 + digit
            simpan //=10
        return balik == x