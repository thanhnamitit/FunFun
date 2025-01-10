class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        prev = 0
        result = 0
        for i in reversed(range(len(s))):
            val = map[s[i]]
            if prev == 0 or val >= prev:
                result += val
            else:
                result -= val
            prev = val
        return result


print(Solution().romanToInt('III'))
print(Solution().romanToInt('LVIII'))
print(Solution().romanToInt('MCMXCIV'))
