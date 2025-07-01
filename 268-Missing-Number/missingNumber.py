class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        if sorted_nums[0] != 0:
            return 0
        else:
            for i in range(len(sorted_nums) - 1):
                if sorted_nums[i] + 1 != sorted_nums[i + 1]:
                    return sorted_nums[i] + 1
            return sorted_nums[-1] + 1