from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(
            word.startswith(pref) for word in words
        )


print(Solution().prefixCount(["pay", "attention", "practice", "attend"], 'at'))
print(Solution().prefixCount(["leetcode", "win", "loops", "success"], 'code'))
