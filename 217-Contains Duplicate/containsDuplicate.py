class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        x = len(nums)
        for i in range (x-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        