from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
        left = 0
        right = 0
        for index in range(1, len(boxes)):
            char = boxes[index]
            if char == '1':
                right += 1
                result[0] += index - 0
                print(result[0])
        for index in range(1, len(boxes)):
            char = boxes[index]
            if char == '1':
                right -= 1
            if boxes[index - 1] == '1':
                left += 1
            result[index] = result[index - 1] - right + left - (1 if char == '1' else 0)

        return result


print(Solution().minOperations("110"))
print(Solution().minOperations("001011"))
