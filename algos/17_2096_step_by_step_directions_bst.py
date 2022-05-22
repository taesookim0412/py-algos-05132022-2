# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    res = ""
    pathForStart = []
    pathForDest = []
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        self.dfs(root, startValue, destValue, path)
        for i in range(max(len(self.pathForStart), len(self.pathForDest))):
            if i >= len(self.pathForStart):
                return ''.join(self.pathForDest[i:])
            elif i >= len(self.pathForDest):
                return ''.join(['U' for _ in range(len(self.pathForStart[i:]))])
            elif self.pathForStart[i] != self.pathForDest[i]:
                return ''.join(['U' for _ in range(len(self.pathForStart[i:]))])  + ''.join(self.pathForDest[i:])


    def dfs(self, root, startValue, destValue, path):
        if root:
            if root.val == startValue:
                self.pathForStart = path.copy()
            elif root.val == destValue:
                self.pathForDest = path.copy()
            path.append("L")
            self.dfs(root.left, startValue, destValue, path)
            path.pop()
            path.append("R")
            self.dfs(root.right, startValue, destValue, path)
            path.pop()



