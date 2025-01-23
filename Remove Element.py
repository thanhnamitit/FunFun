from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        cursor = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cursor] = nums[i]
                cursor += 1
        return cursor


print(Solution().removeElement([3, 2, 2, 3], 3))
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
