#77ms, 72.27%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 2 -> 4 -> 3
# 5 -> 6 -> 4
# returns:
# 7 -> 0 -> 8
# ans: 342 + 564 = 807
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            combined = l1.val + l2.val + carry
            carry = combined // 10
            if carry:
                combined = combined % 10
            curr.next = ListNode(combined)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                combined = l1.val + carry
                carry = combined // 10
                if carry:
                    combined = combined % 10
                curr.next = ListNode(combined)
                curr = curr.next
                l1 = l1.next
        elif l2:
            while l2:
                combined = l2.val + carry
                carry = combined // 10
                if carry:
                    combined = combined % 10
                curr.next = ListNode(combined)
                curr = curr.next
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next