#647kms -> 28.2% faster

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        temp = y
        y = x
        x = temp
        min_y = 500
        min_x = 500
        max_y = -1
        max_x = -1

        # uldr
        y_dirs = [-1, 0, 1, 0]
        x_dirs = [0, -1, 0, 1]

        q = collections.deque()
        q.append([y, x])

        visited = set()
        while q:
            cur_pos = q.popleft()
            cur_y, cur_x = cur_pos
            min_y = min(min_y, cur_y)
            max_y = max(max_y, cur_y)
            min_x = min(min_x, cur_x)
            max_x = max(max_x, cur_x)
            for cur_direction in range(4):
                new_y = cur_y + y_dirs[cur_direction]
                new_x = cur_x + x_dirs[cur_direction]
                if new_y > -1 and new_y < len(image) and new_x > -1 and new_x < len(image[0]) and (
                new_y, new_x) not in visited:
                    visited.add(tuple([new_y, new_x]))
                    if image[new_y][new_x] == "1":
                        q.append([new_y, new_x])
        return (max_y - min_y + 1) * (max_x - min_x + 1)