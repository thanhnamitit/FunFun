from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        start1 = 0
        start2 = 1

        for num in derived:
            if num == 1:
                start1 = 1 - start1
                start2 = 1 - start2

        return start1 == 0 or start2 == 1

print(Solution().doesValidArrayExist([1,1,0]))
print(Solution().doesValidArrayExist([1,1]))
print(Solution().doesValidArrayExist([1,0]))