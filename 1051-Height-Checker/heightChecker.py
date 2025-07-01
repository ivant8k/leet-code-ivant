class Solution(object):
    def heightChecker(self, heights):
        count = 0
        expected = sorted(heights)
        for i in range (len(heights)):
            if heights[i] != expected[i]:
                count +=1
        return count