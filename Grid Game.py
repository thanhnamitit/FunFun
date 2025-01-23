from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix_sum = [0] * (len(grid[0]) + 1)
        suffix_sum = [0] * (len(grid[0]) + 1)

        for i in range(len(grid[0])):
            j = len(grid[0]) - i - 1
            prefix_sum[i + 1] = prefix_sum[i] + grid[1][i]
            suffix_sum[j] = suffix_sum[j + 1] + grid[0][j]
        result = -1
        for i in range(len(grid[0])):
            max_here = max(suffix_sum[i + 1], prefix_sum[i])
            if result > max_here or result == -1:
                result = max_here
        return result


print(Solution().gridGame(
    [[2, 5, 4],
     [1, 5, 1]]))
print(Solution().gridGame([[3, 3, 1], [8, 5, 2]]))
print(Solution().gridGame([[1, 3, 1, 15], [1, 3, 3, 1]]))
