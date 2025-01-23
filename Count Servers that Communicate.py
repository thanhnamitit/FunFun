from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r_map = {}
        c_map = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    i_arr = r_map.get(i, [])
                    i_arr.append([i, j])
                    r_map[i] = i_arr
                    j_arr = c_map.get(j, [])
                    j_arr.append([i, j])
                    c_map[j] = j_arr
        arr = [arr for arr in r_map.values() if len(arr) > 1] + [arr for arr in c_map.values() if len(arr) > 1]
        flattened_arr = [tuple(item) for sublist in arr for item in sublist]
        return len(set(flattened_arr))


print(Solution().countServers([[1, 0], [0, 1]]))
print(Solution().countServers([[1, 0], [1, 1]]))
print(Solution().countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
