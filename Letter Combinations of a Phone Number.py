from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        map = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }
        result = set()
        arr = [0] * len(digits)
        self.dfs(0, digits, map, arr, result)
        return list(result)

    def dfs(self, index, digits, map, arr, result):
        if index == len(digits):
            result.add(
                ''.join([
                    map[int(digits[index])][arr[index]] for index in range(len(digits))
                ])
            )
            return
        number = int(digits[index])
        letters = map[number]
        for i in range(0, len(letters)):
            arr[index] = i
            self.dfs(index + 1, digits, map, arr, result)


print(Solution().letterCombinations('23'))
print(Solution().letterCombinations('2'))
