class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1] and res[-1][1] < interval[1]:
                res[-1][1] = interval[1]
            elif res[-1][1] < interval[1]:
                res.append(interval)
        return res