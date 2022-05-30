#94.31% DFS + DP
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.dp = {}
        wordsSet = set(words)
        for word in words:
            self.dfs(wordsSet, word)
        # print(self.dp)
        return max(self.dp.values())

    def dfs(self, words, currentWord):
        if currentWord in self.dp:
            return self.dp[currentWord]
        maxLen = 1
        for i, char in enumerate(currentWord):
            newWord = currentWord[:i] + currentWord[i + 1:]
            if newWord in words:
                currentLen = 1 + self.dfs(words, newWord)
                maxLen = max(maxLen, currentLen)
        if currentWord in self.dp:
            self.dp[currentWord] = max(self.dp[currentWord], maxLen)
        else:
            self.dp[currentWord] = maxLen
        return maxLen

#incorrect solution: DFS + DP without 'same order' predecessor

class Solution:
    # ['d', 'de', 'def']
    # sorted by lengths.
    # two pointers from len - 1 each
    # isPredecessor
    maxLen = 1
    dp = {}

    def longestStrChain(self, words: List[str]) -> int:
        self.dp = {}
        sortedWords = list(sorted(words, key=len))
        for word in sortedWords:
            res = set()
            res.add(word)
            self.dfs(sortedWords, 0, res)
        return max(self.dp.values())

    def dfs(self, words: List[str], i, res):
        if words[i] in self.dp:
            return self.dp[words[i]]
        maxLen = 1
        for j in range(i + 1, len(words)):
            if self.isPredecessor(words[i], words[j]):
                res.add(words[j])
                self.dp[words[i]] = max(maxLen, 1 + self.dfs(words, j, res))
                maxLen = max(maxLen, self.dp[words[i]])
                res.remove(words[j])
        return maxLen

    def isPredecessor(self, shorterWord, longerWord):
        if len(longerWord) - len(shorterWord) != 1:
            return False
        shorterWordCtr = collections.Counter(shorterWord)
        longerWordCtr = collections.Counter(longerWord)

        # print(shorterWord, longerWord)

        data = longerWordCtr - shorterWordCtr
        if len(data) == 1:
            for k in data:
                if data[k] == 1:
                    # print(shorterWord, longerWord)
                    return True
        return False


#incorrect solution - dfs without 'same order' predecessor
class Solution:
    # ['d', 'de', 'def']
    # sorted by lengths.
    # two pointers from len - 1 each
    # isPredecessor
    maxLen = 1

    def longestStrChain(self, words: List[str]) -> int:
        dp = [0 for _ in range(len(words))]
        sortedWords = list(sorted(words, key=len))
        for word in sortedWords:
            res = set()
            res.add(word)
            self.dfs(sortedWords, 0, res)
        return self.maxLen

    def dfs(self, words: List[str], i, res):
        self.maxLen = max(self.maxLen, len(res))
        for j in range(i + 1, len(words)):
            if self.isPredecessor(words[i], words[j]):
                res.add(words[j])
                self.dfs(words, j, res)
                res.remove(words[j])

    def isPredecessor(self, shorterWord, longerWord):
        if len(longerWord) - len(shorterWord) != 1:
            return False
        shorterWordCtr = collections.Counter(shorterWord)
        longerWordCtr = collections.Counter(longerWord)

        # print(shorterWord, longerWord)

        data = longerWordCtr - shorterWordCtr
        if len(data) == 1:
            for k in data:
                if data[k] == 1:
                    # print(shorterWord, longerWord)
                    return True
        return False