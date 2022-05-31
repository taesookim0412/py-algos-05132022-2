import collections


class Solution:
    def decimalToBinary(self, num):
        res = collections.deque()
        while num > 0:
            res.appendleft(str(num % 2))
            num = num // 2
        return ''.join(res)

    def decimalToBinaryRecursive(self, num):
        res = []
        self.traverse(num, res)
        return ''.join(res)

    def traverse(self, num, res):
        if num == 0:
            return
        remainder = num % 2
        self.traverse(num // 2, res)
        res.append(str(remainder))

s = Solution()
print(
    s.decimalToBinary(42),
    s.decimalToBinaryRecursive(42),
    s.decimalToBinary(41),
    s.decimalToBinaryRecursive(41),
    s.decimalToBinary(123),
    s.decimalToBinaryRecursive(123),
)