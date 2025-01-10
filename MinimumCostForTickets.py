from typing import List


class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * len(days)
        self.dfs(days, costs, 0, dp)
        return dp[0]

    def dfs(self, days: List[int], costs: List[int], todayIndex: int, dp: List[int]) -> int:
        length = len(days)
        if todayIndex >= length:
            return 0
        if dp[todayIndex] != 0:
            return dp[todayIndex]

        next_7_day_index = length
        next_30_day_index = length
        for i in range(todayIndex + 1, length):
            if days[i] >= days[todayIndex] + 7 and next_7_day_index == length:
                next_7_day_index = i
            if days[i] >= days[todayIndex] + 30:
                next_30_day_index = i
                break
        result = min([
            costs[2] + self.dfs(days, costs, next_30_day_index, dp),
            costs[1] + self.dfs(days, costs, next_7_day_index, dp),
            costs[0] + self.dfs(days, costs, todayIndex + 1, dp),
        ])
        dp[todayIndex] = result
        return result


print(Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
print(Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
print(Solution().mincostTickets(
    [3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 21, 23, 25, 26, 27, 29, 30, 33, 34, 35, 36, 38, 39, 40, 42, 45, 46,
     47, 48, 49, 51, 53, 54, 56, 57, 58, 59, 60, 61, 63, 64, 67, 68, 69, 70, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 85,
     88, 91, 92, 93, 96],
    [3, 17, 57]

)
)
