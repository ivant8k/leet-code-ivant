class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        current_sum = 0
        for num in nums:
            current_sum += num
            ans.append(current_sum)
        return ans