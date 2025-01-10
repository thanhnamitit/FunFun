class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        while "**" in p:
            p = p.replace('**', '*')
        if p == '*':
            return True

        if '*' not in p:
            return len(s) == len(p) and self.indexOf(s, p, 0) == 0

        splits = p.split('*')
        if len(splits[0]) + len(splits[-1]) > len(s):
            return False
        if splits[0]:
            for index, char in enumerate(splits[0]):
                if char == '?':
                    continue
                if s[index] != char:
                    return False
            s = s[len(splits[0]):]
        splits = splits[1:]
        if splits[-1]:
            for index, char in enumerate(splits[-1]):
                if char == '?':
                    continue
                if s[len(s) - len(splits[-1]) + index] != char:
                    return False
            s = s[:len(s) - len(splits[-1])]
        splits = splits[:len(splits) - 1]
        while len(splits) != 0:
            found = self.indexOf(s, splits[0], 0)
            if found == -1:
                return False
            s = s[found + len(splits[0]):]
            splits = splits[1:]

        return True

    def indexOf(self, s, target, start):
        if len(target) > len(s):
            return -1
        for i in range(start, len(s) - len(target) + 1):
            sum = 0
            for j in range(0, len(target)):
                if target[j] == '?' or target[j] == s[i + j]:
                    sum += 1
                else:
                    break
            if sum == len(target):
                return i

        return -1

    def dfs(self, s, splits):
        if len(splits) == 0:
            return True
        found = self.indexOf(s, splits[0], 0)
        while found != -1:
            if self.dfs(s[found + len(splits[0]):], splits[1:]):
                return True
            found = self.indexOf(s, splits[0], found + 1)
        return False


print(Solution().isMatch("abc", "*abc?*") == False)
print(Solution().isMatch("mississippi", "m??*ss*?i*pi") == False)
print(Solution().isMatch("ab", "*?*?*") == True)
print(Solution().isMatch("abcabczzzde", "*abc???de*") == True)
print(Solution().isMatch(
    "aaaabaabaabbbabaabaabbbbaabaaabaaabbabbbaaabbbbbbabababbaabbabbbbaababaaabbbababbbaabbbaabbaaabbbaabbbbbaaaabaaabaabbabbbaabababbaabbbabababbaabaaababbbbbabaababbbabbabaaaaaababbbbaabbbbaaababbbbaabbbbb",
    "**a*b*b**b*b****bb******b***babaab*ba*a*aaa***baa****b***bbbb*bbaa*a***a*a*****a*b*a*a**ba***aa*a**a*"))
#
#
# print(Solution().isMatch("adceb", "*a*b"))
#
# print(Solution().isMatch("aa", "a"))
# print(Solution().isMatch("aa", "*"))
# print(Solution().isMatch("cb", "?a"))
# print(Solution().isMatch("acdcb", "a*c?b"))
# print(Solution().isMatch("acdcb", "a*?b"))
# print(Solution().isMatch("adceb", "*a*b"))
# print(Solution().isMatch("", "******"))
# print(Solution().isMatch("ho", "ho**"))
# print(Solution().isMatch(
#     "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
#     "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
# ))
# print(Solution().isMatch(
#     "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
#     "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
#
# s = 'babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb'
# # print(s.find('ab', 0))
