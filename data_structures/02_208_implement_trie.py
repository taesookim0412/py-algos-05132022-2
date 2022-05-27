#214ms 60%

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        i = 0
        cur = self.trie
        while i < len(word):
            if word[i] in cur:
                cur = cur[word[i]]
            else:
                cur[word[i]] = {}
                cur = cur[word[i]]
            i += 1
        cur['tail'] = True

    def search(self, word: str) -> bool:
        # print(self.trie)
        if len(word) == 0:
            return False
        i = 0
        cur = self.trie
        while i < len(word) and word[i] in cur:
            cur = cur[word[i]]
            i += 1
        return i == len(word) and 'tail' in cur and cur['tail'] is True

    def startsWith(self, prefix: str) -> bool:
        # print(self.trie)
        if len(prefix) == 0:
            return False
        i = 0
        cur = self.trie
        while i < len(prefix) and prefix[i] in cur:
            cur = cur[prefix[i]]
            i += 1
        isPrefix = 'tail' not in cur
        return i == len(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)