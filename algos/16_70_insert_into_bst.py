# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.dfs(root, val)
        return root

    def dfs(self, root, insertVal):
        if not root:
            return TreeNode(insertVal)
        if root:
            #if insertVal == root.val:
                # return root
            if insertVal < root.val:
                root.left = self.dfs(root.left, insertVal)
            elif insertVal > root.val:
                root.right = self.dfs(root.right, insertVal)
            return root