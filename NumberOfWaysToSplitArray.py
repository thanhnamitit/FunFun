from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for index, num in enumerate(nums):
            prefix_sum[index + 1] = prefix_sum[index] + num

        print(prefix_sum)

        result = 0
        for i in range(1, len(prefix_sum) - 1):
            if prefix_sum[-1] - prefix_sum[i] <= prefix_sum[i]:
                result += 1
        return result


print(Solution().waysToSplitArray([10, 4, -8, 7]) == 2)
print(Solution().waysToSplitArray([2, 3, 1, 0]) == 2)
print(Solution().waysToSplitArray([6, -1, 9]) == 0)
print(Solution().waysToSplitArray([0,0]) == 1)
