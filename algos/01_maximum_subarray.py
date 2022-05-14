class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = -1 * sys.maxsize
        for num in nums:
            local_max = max(local_max + num, num)
            global_max = max(global_max, local_max)
        return global_max
