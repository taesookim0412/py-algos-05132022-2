#47ms 34.95% (estimate)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rts = [root]
        lfts = []
        res = []
        while rts:
            curNode = rts.pop()
            if curNode:
                while curNode:
                    lfts.append(curNode)
                    curNode = curNode.left
                while lfts:
                    curLft = lfts.pop()
                    res.append(curLft.val)
                    if curLft.right:
                        rts.append(curLft.right)
                        break
        return res