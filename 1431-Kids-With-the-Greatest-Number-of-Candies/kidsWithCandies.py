class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = 0
        output =[]
        for i in range (len(candies)):
            if max_candies <= candies[i]:
                max_candies = candies[i]
        for i in range (len(candies)):
            if candies[i] + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output