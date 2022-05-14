class Solution:
    def isValid(self, s: str) -> bool:
        openers = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i, c in enumerate(s):
            if c in close_to_open:
                if len(openers) == 0:
                    return False
                if openers[-1] != close_to_open[c]:
                    return False
                openers.pop()
            else:
                openers.append(c)
        return len(openers) == 0
