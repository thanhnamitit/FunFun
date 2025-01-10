from typing import List


class Solution:

    def create_lps(self, pattern):
        result = [0] * len(pattern)
        count = 0
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[count]:
                count += 1
                result[i] = count
            else:
                count = 0
        return result

    def is_match(self, s, p):
        lps = self.create_lps(p)
        i, j = 0, 0
        while i < len(s):
            if s[i] == p[j]:
                i += 1
                j += 1
                if j == len(p):
                    return True
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if i != j:
                    s, p = (words[i], words[j]) if len(words[i]) > len(words[j]) else (words[j], words[i])
                    if self.is_match(s, p):
                        result.add(p)

        return list(result)

print(Solution().stringMatching(["mass", "as", "hero", "superhero"]))
print(Solution().stringMatching(["leetcode", "et", "code"]))
print(Solution().stringMatching(["blue", "green", "bu"]))
