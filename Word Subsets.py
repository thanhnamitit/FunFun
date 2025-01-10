from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        global_char_map = {}
        result = set(words1)
        for word2 in words2:
            for char in word2:
                count = word2.count(char)
                if char not in global_char_map or global_char_map[char] < count:
                    global_char_map[char] = count

        for word in words1:
            for value in global_char_map:
                if word.count(value) < global_char_map[value]:
                    result.remove(word)
                    break
        return list(result)


print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]))
print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"]))
print(Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]))
