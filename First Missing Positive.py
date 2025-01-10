from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] < n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1


print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
print(Solution().firstMissingPositive([3, 4, -1, 1]))
print(Solution().firstMissingPositive([1, 2, 0]))
print(Solution().firstMissingPositive([3, 2, 0]))
print(Solution().firstMissingPositive([1]))
print(Solution().firstMissingPositive([0, 2, 2, 1, 1]))
