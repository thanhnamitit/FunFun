from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        if len(mat[0]) == 0:
            return len(mat)
        rc_map = {}

        for i in range(len(mat)):
            for j in range(len(mat[1])):
                rc_map[mat[i][j]] = [i, j]

        r_map = {}
        c_map = {}

        for index, num in enumerate(arr):
            rc = rc_map[num]
            r_map[rc[0]] = r_map.get(rc[0], 0) + 1
            if r_map[rc[0]] == len(mat[0]):
                return index
            c_map[rc[1]] = c_map.get(rc[1], 0) + 1
            if c_map[rc[1]] == len(mat):
                return index

        return len(mat[0])


print(Solution().firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]))
print(Solution().firstCompleteIndex([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]))
