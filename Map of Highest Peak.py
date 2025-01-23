from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = []
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append([i, j])
        rows = len(isWater)
        cols = len(isWater[0])
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        result = [[0] * cols for i in range(rows)]
        while len(queue) != 0:
            top = queue.pop(0)
            for direction in directions:
                x = top[0] + direction[0]
                y = top[1] + direction[1]
                if 0 <= x < rows and 0 <= y < cols and isWater[x][y] == 0 and result[x][y] == 0:
                    result[x][y] = result[top[0]][top[1]] + 1
                    queue.append([x, y])

        return result


#
print(Solution().highestPeak([[0, 1], [0, 0]]))
print(Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
print(Solution().highestPeak([[1]]))
