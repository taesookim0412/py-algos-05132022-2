# wrong answer (138/178)
# does not consider duplicates nor is it stated in the prompt.

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changedSet = set(changed)
        res = []
        for num in changed:
            if num in changedSet and num * 2 in changedSet:
                res.append(num)
                changedSet.remove(num)
                if num != 0:
                    changedSet.remove(num * 2)
        if len(changedSet) == 0:
            return res
        return []