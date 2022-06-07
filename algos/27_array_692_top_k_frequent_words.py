#84ms, 40.73% --> heapify the array by inbuilt nsmallest
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        seen = {}
        for word in words:
            wordCount = seen.get(word, 0) + 1
            seen[word] = wordCount
        pq = []
        for wrd, ct in seen.items():
            pq.append((-1 * ct, wrd))
        return [data[1] for data in heapq.nsmallest(k, pq)]

# 116ms, 9.17%
# heap push is slow

class Solution:
    # ['word1', 'word2', 'word1']
    # seen: {word: ct}
    # i = 0:
    # seen: {}
    # heapq.heappush(pq, [-1 * seen[word], word])
    # seen[word] = seen.get(word, 0) + 1
    # return we'll iterate heappop()
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = []
        seen = {}
        for word in words:
            wordCount = seen.get(word, 0) + 1
            seen[word] = wordCount
            heapq.heappush(pq, [-1 * wordCount, word])
        seen = set()
        res = []
        while len(res) < k and pq:
            cur = heapq.heappop(pq)
            amt, word = cur
            if word not in seen:
                res.append(word)
                seen.add(word)
            # print(seen)
        return res

