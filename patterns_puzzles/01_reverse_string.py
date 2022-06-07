#Option A: In-built reverse

#Option B: Iterative n//2 swap
# 253ms 46.34%
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # store last index to increase performance by about 25% - 50%
        lastIdx = len(s) - 1
        for i in range(len(s) // 2):
            # Pythonically swap without a temp variable.
            s[i], s[lastIdx - i] = s[lastIdx - i], s[i]

# Option C Optimized: two-pointer
# 213ms, 76.54%
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lastIdx = len(s) - 1
        l = 0
        last = len(s) // 2
        while l < last:
            s[l], s[lastIdx - l] = s[lastIdx - l], s[l]
            l += 1

# Option C: two-pointer
# 416ms 6.27%
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1