#170ms, 55.38%

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # manhattan distance
        if k >= len(grid) + len(grid[0]) - 2:
            return len(grid) + len(grid[0]) - 2
        # rdlu
        # yDirs = [0, 1, 0, -1]
        # xDirs = [1, 0, -1, 0]
        xDirs = [0, 1, 0, -1]
        yDirs = [1, 0, -1, 0]

        # y, x, traveledDistance, remainingBreaks
        q = collections.deque()
        q.append([0,0,0,k])

        visited = set()
        visited.add("0,0,k")

        while q:
            currentPos = q.popleft()
            y, x, traveledDistance, remainingBreaks = currentPos
            if y == len(grid) - 1 and x == len(grid[0]) - 1:
                return traveledDistance
            for currentDirection in range(4):
                newY = y + yDirs[currentDirection]
                newX = x + xDirs[currentDirection]
                if newY > -1 and newY < len(grid) and newX > -1 and newX < len(grid[0]):
                    newRemainingBreaks = remainingBreaks
                    if grid[newY][newX] == 1:
                        newRemainingBreaks -= 1
                    if newRemainingBreaks < 0:
                        continue
                    if f"{newY},{newX},{newRemainingBreaks}" not in visited:
                        visited.add(f"{newY},{newX},{newRemainingBreaks}")
                        q.append([newY, newX, traveledDistance + 1, newRemainingBreaks])
        return -1