# Recursive,  95.13%, 95.75%

class Solution:
    def __init__(self):
        self.ctr = 0

    def getDecimalValue(self, head: ListNode) -> int:
        res = [0]
        self.traverse(head, res)
        return res[-1]

    def traverse(self, cur, res):
        if cur:
            self.traverse(cur.next, res)
            res[-1] = res[-1] + (cur.val * ( 2 ** self.ctr))
            self.ctr += 1

# Double pass

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        res = 0
        for i, num in enumerate(reversed(nums)):
            res += num * (2 ** i)
        return res