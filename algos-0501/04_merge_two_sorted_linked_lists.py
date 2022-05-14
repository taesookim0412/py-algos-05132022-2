# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        left = list1
        right = list2
        while left and right:
            if right.val < left.val:
                curr.next = right
                right = right.next
            else:
                curr.next = left
                left = left.next
            curr = curr.next
        if left:
            curr.next = left
        elif right:
            curr.next = right
        return dummy.next