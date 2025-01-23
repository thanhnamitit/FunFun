from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        if len(nums1) % 2 == 1:
            for num in nums2:
                result = result ^ num
        if len(nums2) % 2 == 1:
            for num in nums1:
                result = result ^ num
        return result


print(Solution().xorAllNums([2, 1, 3], [10, 2, 5, 0]))
