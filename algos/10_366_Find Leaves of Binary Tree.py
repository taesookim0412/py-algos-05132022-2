# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_map = {}
        self.traverse(root, nodes_map)
        return nodes_map.values()

    def traverse(self, root, nodes_map):
        if root:
            l = self.traverse(root.left, nodes_map)
            r = self.traverse(root.right, nodes_map)

            node_height = max(1 + l, 1 + r)

            if node_height not in nodes_map:
                nodes_map[node_height] = [root.val]
            else:
                nodes_map[node_height].append(root.val)
            return node_height
        return -1

