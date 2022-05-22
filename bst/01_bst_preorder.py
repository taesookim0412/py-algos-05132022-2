#19ms 99.83%

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        rts = [root]
        stck = []
        res = []
        while rts:
            cur = rts.pop()
            if cur:
                res.append(cur.val)
                rts.append(cur.right)
                stck.append(cur.left)
                while stck:
                    curLft = stck.pop()
                    if curLft:
                        res.append(curLft.val)
                        rts.append(curLft.right)
                        stck.append(curLft.left)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        rts = [root]
        stck = []
        while rts:
            curNode = rts.pop()
            res.append(curNode.val)
            if curNode.right:
                rts.append(curNode.right)
            if curNode.left:
                stck.append(curNode.left)
            while stck:
                curLft = stck.pop()
                if curLft.right:
                    rts.append(curLft.right)
                if curLft.left:
                    stck.append(curLft.left)
                res.append(curLft.val)
        return res

# 'simplified' solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stck = [root]
        res = []
        while stck:
            cur = stck.pop()
            if cur:
                res.append(cur.val)
                stck.append(cur.right)
                stck.append(cur.left)
        return res