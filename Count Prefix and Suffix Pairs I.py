from typing import List


class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        if len(str2) > len(str1):
            return False
        for i in range(0, len(str2)):
            if str1[i] != str2[i] or str1[len(str1) - 1 - i] != str2[len(str2) - 1 - i]:
                return False

        return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                str1, str2 = (words[j], words[i])
                if self.isPrefixAndSuffix(str1, str2):
                    result += 1
        return result


print(Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
print(Solution().countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
print(Solution().countPrefixSuffixPairs(["abab", "ab"]))
print(Solution().countPrefixSuffixPairs(["ba", "c", "aaa", "baa"]))
