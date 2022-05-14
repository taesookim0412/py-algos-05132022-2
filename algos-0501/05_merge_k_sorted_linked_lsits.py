# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for node in lists:
            while node:
                vals.append(node)
                node = node.next
        vals.sort(key=lambda x: x.val)

        dummy = ListNode(0)
        curr = dummy
        for val in vals:
            curr.next = val
            curr = curr.next
        return dummy.next