class Solution(object):
    def isThree(self, n):
        count = 0
        i = 1
        while i<=n:
            if n%i == 0:
                count+=1
            i+=1
        return count == 3
        