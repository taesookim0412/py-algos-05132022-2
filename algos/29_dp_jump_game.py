# 636ms 54.10%

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        ctr = 1
        for i, num in enumerate(nums):
            if ctr == 0:
                return False
            ctr = max(ctr - 1, num)
        return True