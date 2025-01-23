class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin1 = bin(num1)[2:]
        bin2 = bin(num2)[2:]
        bin1 = bin1.zfill((((len(bin1) + 3) // 4) * 4))
        bin2 = bin2.zfill((((len(bin2) + 3) // 4) * 4))
        set_bits = len([i for i in bin2 if i == '1'])
        bin_answer = [0] * len(bin1)
        if set_bits > 0:
            for i in range(len(bin1)):
                bin_answer[i] = 1 if bin1[i] == '1' else 0
                if bin_answer[i] == 1:
                    set_bits -= 1
                    if set_bits == 0:
                        break
        if set_bits > 0:
            for i in reversed(range(len(bin1))):
                if bin_answer[i] == 0:
                    bin_answer[i] = 1
                    set_bits -= 1
                    if set_bits == 0:
                        break
        if set_bits > 0:
            bin_answer = [1] * set_bits + bin_answer
        return int(''.join(map(str, bin_answer)), 2)


print(Solution().minimizeXor(3, 5))
print(Solution().minimizeXor(1, 12))
