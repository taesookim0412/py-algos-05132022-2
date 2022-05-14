#40ms, 53.88% faster, 13.9, 83.29% less
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # rdlu
        y_pos = [0, 1, 0, -1]
        x_pos = [1, 0, -1, 0]

        cur_y = 0
        cur_x = 0

        cur_direction = 0

        ctr = 0
        num_elems = len(matrix) * len(matrix[0])

        res = [0 for _ in range(num_elems)]

        visited = set()
        while ctr < num_elems:
            res[ctr] = matrix[cur_y][cur_x]
            ctr += 1
            visited.add(tuple([cur_y, cur_x]))
            cur_y += y_pos[cur_direction]
            cur_x += x_pos[cur_direction]
            if cur_y >= len(matrix) or cur_y < 0 or cur_x >= len(matrix[0]) or cur_x < 0 or (cur_y, cur_x) in visited:
                cur_y -= y_pos[cur_direction]
                cur_x -= x_pos[cur_direction]
                cur_direction = (cur_direction + 1) % 4
                cur_y += y_pos[cur_direction]
                cur_x += x_pos[cur_direction]

        return res
