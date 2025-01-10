class Solution:
    def intToRoman(self, num: int) -> str:
        multiple = 0
        answer = ''
        while num > 0:
            answer = f'{self.toRoman(num % 10, multiple)}{answer}'
            num //= 10
            multiple += 1
        return answer

    def toRoman(self, num, multiple):

        rules = [
            ['I', 'V'],
            ['X', 'L'],
            ['C', 'D'],
            ['M', ''],
        ]
        rule = rules[multiple]
        if num <= 3:
            return rule[0] * num
        elif num == 4:
            return f'{rule[0]}{rule[1]}'
        elif num < 9:
            return f'{rule[1]}{rule[0] * (num - 5)}'
        else:
            return f'{rule[0]}{rules[multiple + 1][0]}'


print(Solution().intToRoman(3749))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
