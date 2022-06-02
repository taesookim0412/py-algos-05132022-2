# Rabin-Karp Rolling Hash 73/81 based on https://leetcode.com/problems/strings-differ-by-one-character/discuss/2065237/JAVA-HASHCODE ,
# https://leetcode.com/problems/strings-differ-by-one-character/discuss/803030/JACA-Using-Hash-Rabin-Karp,
# https://leetcode.com/problems/strings-differ-by-one-character/discuss/2081505/Python3-O(MN)-solution-with-detailed-explanation

class Solution:
    hashMod = 719
    largeHashMod = 10000000007

    def differByOne(self, lst: List[str]) -> bool:
        wordLen = len(lst[0])

        powerLst = [1 for _ in range(wordLen + 1)]
        for i in range(len(powerLst) - 1):
            powerLst[i + 1] = (powerLst[i] * self.hashMod) % self.largeHashMod

        hashMultiplier = [0 for _ in range(len(lst))]
        for i, word in enumerate(lst):
            for char in word:
                hashMultiplier[i] = (hashMultiplier[i] * self.hashMod + ord(char)) % self.largeHashMod

        # set of 'w*rds'
        seen = set()
        for i, word in enumerate(lst):
            for j, ch in enumerate(word):
                newHash = (hashMultiplier[i] - ord(ch) * powerLst[wordLen - j - 1]) % self.largeHashMod
                if newHash in seen:
                    return True
                seen.add(newHash)
        return False


# brute force tle

class Solution:
    def differByOne(self, lst: List[str]) -> bool:
        for i, word in enumerate(lst):
            for word2 in lst[i + 1:]:
                for i in range(len(word)):
                    if word2[:i] + word2[i + 1:] == word[:i] + word[i + 1:]:
                        return True
        return False