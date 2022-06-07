class Solution:
    # urdl
    yDirections = [-1, 0, 1, 0]
    xDirections = [0, 1, 0, -1]

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.backtrack(set(), robot, 0, 0, 0)

    def backtrack(self, visited, robot, y, x, currentDirection):
        visited.add(f"{y},{x}")
        robot.clean()

        for i in range(4):
            newDirection = (currentDirection + i) % 4
            newY = y + self.yDirections[newDirection]
            newX = x + self.xDirections[newDirection]
            newPos = f"{newY},{newX}"
            if newPos not in visited and robot.move():
                self.backtrack(visited, robot, newY, newX, newDirection)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            robot.turnRight()