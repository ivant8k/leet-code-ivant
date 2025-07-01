class Solution(object):
    def romanToInt(self, s):
        romanDict={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        i = 0
        while i < len(s):
            a = romanDict[s[i]]
            b = 0
            if (i + 1) < len(s):
                b = romanDict[s[i+1]]
            if a < b:
                total -= a
            else:
                total += a
            i+=1
        return total
        