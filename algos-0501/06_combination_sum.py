class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        self.backtrack(candidates, 0, target, [], res, 0)
        return res

    def backtrack(self, candidates, cur, target, cur_arr, res, i):
        if cur == target:
            res.add(tuple(cur_arr))
            return
        if cur > target:
            return
        for j in range(i, len(candidates)):
            self.backtrack(candidates, cur + candidates[j], target, cur_arr + [candidates[j]], res, j)