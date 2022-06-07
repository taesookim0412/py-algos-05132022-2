# lesson learned: greedily using DFS can lead to very incorrect solutions:
# use bfs instead when possible.

# fixed up and incorrect, greedy solution
# class Solution:
#     def racecar(self, target: int) -> int:
#         path = []
#         dp = {}
#         self.pos = 0
#         self.speed = 1
#         self.target = target
#         self.dfs(path, dp)
#         print(dp)
#         return dp[target]
#
#     # dp[pos] = min(dp[pos], len(path))
#     def dfs(self, path, dp):
#         if self.pos == -1 or len(path) > self.target * 3:
#             return 999999
#         if self.pos in dp:
#             return dp[self.pos]
#
#         minLen = 99999
#         # instruction: 'A'
#         tempPos = self.pos
#         tempSpeed = self.speed
#         self.pos += self.speed
#         self.speed *= 2
#         minLen = min(minLen, self.dfs(path + ['A'], dp) - 1)
#
#         self.pos = tempPos
#         self.speed = tempSpeed
#
#         # instruction: 'R'
#         if self.speed > 0:
#             self.speed = -1
#         else:
#             self.speed = 1
#         minLen = min(minLen, self.dfs(path + ['R'], dp) - 1)
#         self.speed = tempSpeed
#
#         if self.pos in dp:
#             dp[self.pos] = min(dp[self.pos], minLen)
#         else:
#             dp[self.pos] = minLen
#         print(f"returning {minLen} from {self.pos}, {path}")
#
#         return len(path)
