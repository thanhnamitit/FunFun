from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mapA = {}
        mapB = {}
        count = 0
        result = [0] * len(A)
        for i in range(len(A)):
            if mapA.get(B[i]) == 1:
                count += 1
            mapB[B[i]] = mapB.get(B[i], 0) + 1

            if mapB.get(A[i]) == 1:
                count += 1
            mapA[A[i]] = mapA.get(A[i], 0) + 1

            result[i] = count
        return result


print(Solution().findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]))
print(Solution().findThePrefixCommonArray([2, 3, 1], [3, 1, 2]))
