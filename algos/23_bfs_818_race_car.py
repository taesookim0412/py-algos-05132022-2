# lesson learned: greedily using DFS can lead to very incorrect solutions:
# use bfs instead when possible.

# class Solution:
#     def racecar(self, target: int) -> int:
#         path = []
#         dp = {}
#         self.pos = 0
#         self.speed = 1
#         self.target = target
#         self.dfs(path, dp)
#         # print(dp)
#         return dp[target]
#
#     # dp[pos] = min(dp[pos], len(path))
#     def dfs(self, path, dp):
#         if self.pos == -1 or len(path) > self.target:
#             return 999999
#         if self.pos in dp:
#             return dp[self.pos]
#         # instruction: 'A'
#         tempPos = self.pos
#         tempSpeed = self.speed
#         self.pos += self.speed
#         self.speed *= 2
#         self.dfs(path + ['A'], dp)
#
#         self.pos = tempPos
#         self.speed = tempSpeed
#
#         # instruction: 'R'
#         if self.speed > 0:
#             self.speed = -1
#         else:
#             self.speed = 1
#         self.dfs(path + ['R'], dp)
#         self.speed = tempSpeed
#
#         if self.pos in dp:
#             dp[self.pos] = min(self.pos, len(path))
#         else:
#             dp[self.pos] = len(path)
