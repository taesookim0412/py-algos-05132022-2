#982ms

class Solution:
    min_y = 500
    max_y = -1
    min_x = 500
    max_x = -1

    # dfs the coords unvisited
    # keep track of y, x. Keep track of min y/x, max y/x
    # return (max_y - min_y) *  (max_x - min_x)
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        temp = y
        y = x
        x = temp
        visited = set()
        self.dfs(image, y, x, visited)
        return (self.max_y - self.min_y + 1) * (self.max_x - self.min_x + 1)

    def dfs(self, image, y, x, visited):
        if y > -1 and y < len(image) and x > -1 and x < len(image[0]) and (y, x) not in visited:
            visited.add(tuple([y, x]))
            if image[y][x] == "1":
                self.min_y = min(self.min_y, y)
                self.max_y = max(self.max_y, y)
                self.min_x = min(self.min_x, x)
                self.max_x = max(self.max_x, x)
                self.dfs(image, y - 1, x, visited)
                self.dfs(image, y + 1, x, visited)
                self.dfs(image, y, x - 1, visited)
                self.dfs(image, y, x + 1, visited)
