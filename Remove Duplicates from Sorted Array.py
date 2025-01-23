from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cursor = 0
        k = 1
        for i in range(1, len(nums)):
            if nums[cursor] != nums[i]:
                nums[cursor + 1] = nums[i]
                cursor += 1
                k += 1
        return k


print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
