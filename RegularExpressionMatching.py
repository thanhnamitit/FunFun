class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        for char in p:
            if char != '*':
                while f'{char}*{char}*' in p:
                    p = p.replace(f'{char}*{char}*', f'{char}*')
        if not p and not s:
            return True
        validated = -1
        for index, char in enumerate(p):
            if index + 1 < len(p) and p[index + 1] == '*':
                if self.isMatch(s[max(0, index):], p[index + 2:]):
                    return True
                for i in range(index, len(s)):
                    if char == '.' or char == s[i]:
                        if self.isMatch(s[i + 1:], p[index + 2:]):
                            return True
                    else: return False
            elif index >= len(s):
                return False
            elif char == '.' or char == s[index]:
                validated = index
            else:
                return False
        return validated == len(s) - 1


print(Solution().isMatch('aaaaaaaaaaaaaaaaaaab', "a*a*a*a*a*a*a*a*a*a*") == False)
print(Solution().isMatch('bbab', "b*a*") == False)
print(Solution().isMatch('aab', "a*b") == True)
print(Solution().isMatch('aab', "c*a*b") == True)
print(Solution().isMatch('mississippi', "mis*is*p*.") == False)
print(Solution().isMatch('aa', 'a') == False)
print(Solution().isMatch('aa', 'a*') == True)
print(Solution().isMatch('ab', '.*') == True)
print(Solution().isMatch('ab', 'a*ab') == True)
