#

class Solution:
    def decodeString(self, s: str) -> str:
        repeats = [[]]
        letters_arr = [[]]
        res = []
        i = 0
        while i < len(s):
            # print(repeats, letters_arr)
            char = s[i]
            if char == '[':
                i += 1
                continue
            if char != ']':
                if char.isnumeric():
                    while char.isnumeric() and i < len(s):
                        repeats[-1].append(char)
                        i += 1
                        if i < len(s):
                            char = s[i]
                    repeats[-1] = int(''.join(repeats[-1]))
                    repeats.append([])
                elif char.isalpha():
                    while char.isalpha() and i < len(s):
                        letters_arr[-1].append(char)
                        i += 1
                        if i < len(s):
                            char = s[i]
                    letters_arr[-1] = ''.join(letters_arr[-1])
                    letters_arr.append([])
                    # broke after adding this
                    if len(letters_arr) != len(repeats):
                        repeats[-1] = 1
                        repeats.append([])
            else:
                total_word = ""
                while repeats:
                    print(letters_arr, repeats)
                    letters, repeat_num = letters_arr.pop(), repeats.pop()
                    # print(letters, repeat_num)
                    if repeat_num and letters:
                        combined = letters + total_word
                        total_word = ""
                        for repeat_idx in range(repeat_num):
                            total_word = combined + total_word
                    # print(total_word)
                repeats = [[]]
                letters_arr = [[]]
                res.append(total_word)
                i += 1
        # another addition
        if len(letters_arr) > 1:
            res.append(letters_arr[0])
        #print(res)
        return ''.join(res)

solu = Solution()
a = solu.decodeString("2[a3[bc]]")
# abcbcbcabcbcbc
print(a)
#fails because of unformatted input
#solu.decodeString("2[abc]3[cd]ef")
#solu.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")