from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        index_to_color = {}
        color_to_count = {}

        counting = 0

        for i in range(len(queries)):
            query = queries[i]
            index = query[0]

            old_color = index_to_color.get(index, 0)
            new_color = query[1]

            if old_color == new_color:
                result[i] = counting
                continue

            count_of_old_color = color_to_count.get(old_color, 0)
            count_of_new_color = color_to_count.get(new_color, 0)

            print(index, new_color, old_color, count_of_new_color, color_to_count, )

            if (old_color == 0 or count_of_old_color > 1) and count_of_new_color == 0:
                counting += 1
                print(f'add, {counting}')

            if old_color != 0:
                color_to_count[old_color] = count_of_old_color - 1
                if count_of_old_color == 1 and count_of_new_color > 0:
                    counting -= 1
                    print(f'sub, {counting}')

            result[i] = counting

            index_to_color[index] = new_color
            color_to_count[new_color] = color_to_count.get(new_color, 0) + 1

        return result


# print(Solution().queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]))
# print(Solution().queryResults(4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
# print(Solution().queryResults(1, [[0, 1], [0, 4], [1, 2], [1, 5], [1, 4]]))
# print(Solution().queryResults(1, [[0, 1], [0, 4], [0, 4], [0, 1], [1, 2]]))
print(Solution().queryResults(1, [[0, 1], [1, 4], [1, 1], [1, 4], [1, 1]]))
