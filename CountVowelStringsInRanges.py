from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vovals = {
            'u': True,
            'e': True,
            'o': True,
            'a': True,
            'i': True,
        }
        prefix_sum = [0] * (len(words) + 1)
        for index, word in enumerate(words):
            if word[0] in vovals and word[-1] in vovals:
                add = 1
            else:
                add = 0
            prefix_sum[index + 1] = prefix_sum[index] + add
        result = [0] * len(queries)
        for index, query in enumerate(queries):
            result[index] = prefix_sum[query[1] + 1] - prefix_sum[query[0]]
        return result


print(Solution().vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]))
print(Solution().vowelStrings(["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]))
