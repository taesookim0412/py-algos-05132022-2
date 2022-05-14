# "abba"
# "a":
# res = 1, start = 0 => res = max(res, res - start)
# "abba"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevs = {}
        res = 0
        start = 0
        for i, c in enumerate(s):
            if c in prevs:
                start = max(start, prevs[c] + 1)
            res = max(res, i - start + 1)
            prevs[c] = i
        return max(res, min(len(s), 1))
