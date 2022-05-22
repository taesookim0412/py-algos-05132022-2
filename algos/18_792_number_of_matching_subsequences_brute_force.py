#tle

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        numWords = 0
        for word in words:
            wordPtr = 0
            for i, char in enumerate(s):
                if char == word[wordPtr]:
                    wordPtr += 1
                if wordPtr == len(word):
                    break
            if wordPtr == len(word):
                numWords += 1
        return numWords



