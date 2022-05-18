from typing import List


class Solution:
    res = 9999
    # rdlu
    y_dirs = [0, 1, 0, -1]
    x_dirs = [1, 0, -1, 0]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.dfs(grid, 0, 0, set(), k, 0)
        if self.res == 9999:
            return -1
        return self.res

    def dfs(self, grid, y, x, visited, remaining_breaks, traveled_distance):
        if y == len(grid) - 1 and x == len(grid[0]) - 1:
            self.res = min(self.res, traveled_distance)
        visited.add(f"{y},{x}")
        for cur_direction in range(4):
            new_y = y + self.y_dirs[cur_direction]
            new_x = x + self.x_dirs[cur_direction]
            if new_y > -1 and new_y < len(grid) and new_x > -1 and new_x < len(grid[0]):
                new_remaining_breaks = remaining_breaks
                if grid[new_y][new_x] == 1:
                    new_remaining_breaks = remaining_breaks - 1
                if new_remaining_breaks > -1  and f"{new_y},{new_x}" not in visited:
                    self.dfs(grid, new_y, new_x, visited, new_remaining_breaks, traveled_distance + 1)
        visited.remove(f"{y},{x}")

solu = Solution()
solu.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]],1)