import heapq
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = []
        q.append([0, k, 0, 0])
        # q = [[traveled_distance, remaining_breaks, y, x]]

        # rdlu
        y_dirs = [0, 1, 0, -1]
        x_dirs = [1, 0, -1, 0]

        visited = set()

        while q:
            data = heapq.heappop(q)
            traveled_distance, remaining_breaks, y, x = data
            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                return traveled_distance
            if f"{y},{x},{remaining_breaks}" in visited:
                continue
            visited.add(f"{y},{x},{remaining_breaks}")
            for cur_direction in range(4):
                new_y = y + y_dirs[cur_direction]
                new_x = x + x_dirs[cur_direction]
                # print(visited)
                if new_y > -1 and new_y < len(grid) and new_x > -1 and new_x < len(grid[0]) and f"{new_y},{new_x},{remaining_breaks}" not in visited:
                    if grid[new_y][new_x] == 1:
                        if remaining_breaks == 0:
                            continue
                        remaining_breaks -= 1
                    heapq.heappush(q, [traveled_distance + 1, remaining_breaks, new_y, new_x])
        return -1

solu = Solution()
res = solu.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)
print(res)
