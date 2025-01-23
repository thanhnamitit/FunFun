class Solution:
    def minimumLength(self, s: str) -> int:
        count_arr = [0] * 28
        for char in s:
            count_arr[ord('z') - ord(char)] += 1
        result = 0
        for num in count_arr:
            if num > 0:
                if num % 2 == 1:
                    result += 1
                else:
                    result += 2
        return result


print(Solution().minimumLength('abaacbcbb'))
