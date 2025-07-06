
from collections import Counter
class FindSumPairs(object):
    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_count = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old_val = self.nums2[index]
        self.nums2_count[old_val] -= 1
        if self.nums2_count[old_val] == 0:
            del self.nums2_count[old_val]
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.nums2_count[new_val] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        res = 0
        for num in self.nums1:
            complement = tot - num
            res += self.nums2_count.get(complement, 0)
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)