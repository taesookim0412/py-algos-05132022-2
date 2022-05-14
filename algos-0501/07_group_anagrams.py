class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in res:
                res[sorted_word] = res[sorted_word] + [word]
            else:
                res[sorted_word] = [word]
        return res.values()