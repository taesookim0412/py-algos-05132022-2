# D:

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = [[]]
        lens = []
        current_len = 0
        for i, word in enumerate(words):
            current_len += len(word)
            if current_len > maxWidth:
                lens.append(current_len - len(word))
                current_len = len(word)
                res.append([])
            if current_len != len(word):
                res[-1].append(' ')
                current_len += 1
            if i == len(words) - 1 and len(lens) != len(res):
                lens.append(current_len)
            res[-1].append(word)
        for i, text_arr in enumerate(res):
            if len(text_arr) == 1 and lens[i] != maxWidth:
                text_arr.append(' ')
                lens[i] = lens[i] + 1

        print(res, lens)
        for i, text_arr in enumerate(res[:-1]):
            current_len = lens[i]
            while current_len < maxWidth:
                for j, texts in enumerate(text_arr):
                    if texts.startswith(' ') and current_len < maxWidth:
                        text_arr[j] = texts + ' '
                        current_len += 1

        print(res, lens)
        # left-justify the unmodified last line
        for i in range(lens[-1], maxWidth):
            res[-1][-1] = res[-1][-1] + " "
        return [''.join(texts) for texts in res]
